#!/usr/bin/python3
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pi = 3.14159
        return pi * (self.radius ** 2)
    def perimeter(self):
        pi = 3.14159
        return pi * (self.radius * 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
