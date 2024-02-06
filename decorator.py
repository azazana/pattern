from unittest import TestCase


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def __getattr__(self, item):
        return getattr(self.__dict__['shape'], item)
    def resize(self, factor):
        if isinstance(self.shape, Circle):
            getattr(self.shape, 'resize')(factor)
    def __str__(self):
        return f'{self.shape} has the color {self.color}'


circle = ColoredShape(Circle(5), 'red')
print(circle)
circle.resize(2)
print(circle)
square = ColoredShape(Square(2), 'blue')
print(square)
square.resize(2)
print(square)