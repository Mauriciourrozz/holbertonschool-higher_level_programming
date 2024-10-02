#!/usr/bin/python3
"""
This file contains a function
"""


def read_file(filename=""):
    """
    This function reads a text file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        contenido = f.read()
        print(contenido, end="")