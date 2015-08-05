from __future__ import division

from vector import Vector
from color import Color
from vertex import Vertex
from guamath import interpolate


__author__ = 'gua'


class Canvas(object):
    def __init__(self, width, height, pixels):
        self.width = width
        self.height = height
        self.pixels = pixels

    def clear(self):
        self.pixels.fill(0)

    def put_pixel(self, x, y, color):
        index = int(y) * self.width + int(x)
        self.pixels[index] = color.uint32()

    def draw_point(self, point, color=Color.cyan()):
        """
        :type point: Vector
        :type color: Color
        :return: None
        """
        if 0 <= point.x < self.width and 0 <= point.y < self.height:
            self.put_pixel(point.x, point.y, color)

    def draw_line(self, p1, p2):
        """
        :type p1: Vector
        :type p2: Vector
        """
        # x1, y1, x2, y2 = map(int, [p1.x, p1.y, p2.x, p2.y])
        x1, y1, x2, y2 = [int(i) for i in [p1.x, p1.y, p2.x, p2.y]]

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            xmin, xmax = sorted([x1, x2])
            ratio = 0 if dx == 0 else dy / dx
            for x in range(xmin, xmax):
                y = y1 + (x - x1) * ratio
                self.draw_point(Vector(x, y))
        else:
            ymin, ymax = sorted([y1, y2])
            ratio = 0 if dy == 0 else dx / dy
            for y in range(ymin, ymax):
                x = x1 + (y - y1) * ratio
                self.draw_point(Vector(x, y))

    def draw_scanline(self, va, vb, y):
        x1 = int(va.position.x)
        x2 = int(vb.position.x)
        sign = 1 if x2 > x1 else -1
        factor = 0
        for x in range(x1, x2 + sign * 1, sign):
            if x1 != x2:
                factor = (x - x1) / (x2 - x1)
            color = interpolate(va.color, vb.color, factor)
            self.draw_point(Vector(x, y), color)

    def draw_triangle(self, v1, v2, v3):
        """
        :type v1: Vertex
        :type v2: Vertex
        :type v3: Vertex
        """
        a, b, c = sorted([v1, v2, v3], key=lambda k: k.position.y)
        middle_factor = 0
        if c.position.y - a.position.y != 0:
            middle_factor = (b.position.y - a.position.y) / (c.position.y - a.position.y)
        middle = interpolate(a, c, middle_factor)

        start_y = int(a.position.y)
        end_y = int(b.position.y)
        for y in range(start_y, end_y + 1):
            factor = (y - start_y) / (end_y - start_y) if end_y != start_y else 0
            va = interpolate(a, b, factor)
            vb = interpolate(a, middle, factor)
            self.draw_scanline(va, vb, y)

        start_y = int(b.position.y)
        end_y = int(c.position.y)
        for y in range(start_y, end_y + 1):
            factor = (y - start_y) / (end_y - start_y) if end_y != start_y else 0
            va = interpolate(b, c, factor)
            vb = interpolate(middle, c, factor)
            self.draw_scanline(va, vb, y)

