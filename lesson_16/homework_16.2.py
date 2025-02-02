from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Square(Shape):
    def __init__(self, side: float):
        self.__side = side

    def area(self):
        return (self.__side)**2

    def perimeter(self):
        return self.__side * 4

shapes = [
    Rectangle(3, 6),
    Circle(10),
    Square(11)
]

for shape in shapes:
    print(f'Figure: {shape.__class__.__name__}')
    print(f'  Area: {shape.area():.2f}')
    print(f'  Perimeter: {shape.perimeter():.2f}')
    print()