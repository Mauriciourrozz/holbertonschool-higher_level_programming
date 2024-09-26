#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            radius = abs(radius)
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2
    def perimeter(self):
        return pi * self.radius * 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

def shape_info(shape): #Creo una funcion para llamar al area y perimetro e imprimirlos
    # Llamo a los metodos area y perimetro, los guardo en una variable
    area = shape.area()
    perimeter = shape.perimeter()
    #Imprime los resultados
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
#en el main estan las instancias donde se 
