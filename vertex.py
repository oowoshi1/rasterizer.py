from color import Color

import operator


class Vertex(object):
    def __init__(self, position, color=Color.cyan()):
        """
        :type position: Vector
        :type color: Color
        """
        self.position = position
        self.color = color

    def _operation(self, other, op):
        position = op(self.position, other.position)
        color = op(self.color, other.color)
        return Vertex(position, color)

    def __add__(self, other):
        return self._operation(other, operator.add)

    def __sub__(self, other):
        return self._operation(other, operator.sub)

    def __mul__(self, value):
        position = self.position * value
        color = self.color * value
        return Vertex(position, color)

