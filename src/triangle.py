from .figure import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c
        if 2 * max(a, b, c) >= self.perimeter:
            raise ValueError(f"Can't define a triangle with sides {a}, {b}, {c}")

    name = 'Triangle'

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter/2.0
        return (p*(p - self.a)*(p - self.b)*(p - self.c))**0.5
