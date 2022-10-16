from .figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    name = 'Rectangle'

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def area(self):
        return self.a * self.b
