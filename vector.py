from __future__ import division

import operator


__author__ = 'gua'


class Vector(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = x, y, z

    def _operation(self, other, op):
        x = op(self.x, other.x)
        y = op(self.y, other.y)
        z = op(self.z, other.z)
        return Vector(x, y, z)

    def __add__(self, other):
        return self._operation(other, operator.add)

    def __sub__(self, other):
        return self._operation(other, operator.sub)

    def __mul__(self, value):
        x, y, z = [i * value for i in [self.x, self.y, self.z]]
        return Vector(x, y, z)

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        l = self.length()
        if l == 0:
            return self
        factor = 1 / l
        return self * factor

    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v):
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x * v.z
        z = self.x * v.y - self.y * v.x
        return Vector(x, y, z)

