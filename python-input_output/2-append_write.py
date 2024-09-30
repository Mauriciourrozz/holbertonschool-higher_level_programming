#!/usr/bin/python3
"""
This file open a file and append a string
"""


def append_write(filename="", text=""):
    """
    This function append a string at the end of file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    largo = len(text)
    return largo
