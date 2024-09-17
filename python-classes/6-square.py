#!/usr/bin/python3
"""
This file contains a class
"""


class Square:
    """
    This class represent a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(value, int) and valor >= 0 for valor in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
