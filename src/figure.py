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

        if isinstance(figure, Figure):
            return self.area + figure.area
        raise ValueError("It is not a geometric figure")
