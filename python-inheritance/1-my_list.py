#!/usr/bin/python3
"""
This file contains a class
"""


class MyList(list):
    """
    This class represent a list
    """
    def print_sorted(self):
        lista_ordenada = sorted(self)
        print(lista_ordenada)
