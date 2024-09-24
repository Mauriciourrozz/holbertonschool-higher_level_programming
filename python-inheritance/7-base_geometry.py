#!/usr/bin/python3
"""
This file contains a class
"""


class BaseGeometry:
    """
    This class represent a Base Geometry

    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
