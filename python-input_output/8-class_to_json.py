#!/usr/bin/python3

"""
This file contains a dict
"""


def class_to_json(obj):
    """
    This function return a dictionary description with simple data structure
    """
    diccionario = {}
    diccionario = obj.__dict__
    return diccionario
