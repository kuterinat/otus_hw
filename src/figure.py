from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, *args):

        if any(arg <= 0 for arg in args):
            raise ValueError(f"All figure params should be positive")

    name = 'Figure'

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def add_area(self, figure):

        if hasattr(figure, 'name') and figure.name in ('Triangle', 'Rectangle', 'Square', 'Circle'):
            return self.area + figure.area
        raise ValueError("It is non-geometric figure")
