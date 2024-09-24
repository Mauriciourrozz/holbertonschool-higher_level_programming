#!/usr/bin/python3
"""
This file contains a class
"""


class BaseGeometry:
    """
    This class represent a Base Geometry

    """
    def __init__(self, alto=0, ancho=0):
        self.alto = alto
        self.ancho = ancho

    def area(self):
            raise Exception("area() is not implemented")
