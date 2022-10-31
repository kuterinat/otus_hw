from .rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    name = 'Square'
