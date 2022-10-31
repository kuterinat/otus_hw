import math
from .figure import Figure


class Circle(Figure):

    def __init__(self, r):
        super().__init__(r)
        self.r = r

    name = 'Circle'

    @property
    def area(self):
        return math.pi * self.r**2

    @property
    def perimeter(self):
        return 2 * math.pi * self.r
