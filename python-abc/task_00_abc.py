#!/usr/bin/python3
"""
This file contains a Abstract Class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    This is a Abstract Class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    This is a class that inherits from the Animal class
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This is a class that inherits from the Animal class
    """
    def sound(self):
        return "Meow"
