#!/usr/bin/python3
"""
This file open a file and write a text
"""


def write_file(filename="", text=""):
    """
    Function that counts the characters that prints
    """
    with open(filename, 'x', encoding='utf-8') as f:
        f.write(text)
    count = 0
    for letra in text:
        count += 1
    return count
