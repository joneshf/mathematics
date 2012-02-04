import math
from exceptions import IndexError
from operator import add, mul, neg

class VectorError(IndexError):
    pass

class Vector(object):
    def __init__(self, *args):
        self.values = args

    def __getitem__(self, item):
        try:
            return self.values[item]
        except IndexError:
            raise VectorError('Invalid dimension')

    def __repr__(self):
        values = ', '.join(map(str, self.values))

        return '<{}>'.format(values)

    def __str__(self):
        values = ', '.join(map(str, self.values))

        return '<{}>'.format(values)

    def __add__(self, v2):
        if len(self.values) == len(v2.values):
            new_values = map(add, self.values, v2.values)

            # Unpack the list
            return Vector(*new_values)
        else:
            raise VectorError('Vectors must be the same length.')

    def __mul__(self, scalar):
        new_values = map(lambda x: x * scalar, self.values)

        return Vector(*new_values)

    def __neg__(self):
        new_values = map(neg, self.values)

        # Unpack the list
        return Vector(*new_values)

    def __sub__(self, v2):
        v2 = -v2

        return self.__add__(v2)

    def __rmul__(self, scalar):
        new_values = map(lambda x: scalar * x, self.values)

        return Vector(*new_values)

    def dot(self, v2):
        if len(self.values) == len(v2.values):
            scalar = sum(map(mul, self.values, v2.values))

            return scalar
        else:
            raise VectorError('Vectors must be the same length.')

    def cross(self, v2):
        if 3 == len(self.values) == len(v2.values):
            i = self.values[1] * v2.values[2] - self.values[2] * v2.values[1]
            j = self.values[2] * v2.values[0] - self.values[0] * v2.values[2]
            k = self.values[0] * v2.values[1] - self.values[1] * v2.values[0]

            return Vector(i, j, k)
        else:
            raise VectorError('Both vectors must be in 3-space.')

    def mag(self):

        return pow(self.dot(self), 0.5)

    def angle(self, v2):
        return math.acos(self.dot(v2) / (self.mag() * v2.mag()))
