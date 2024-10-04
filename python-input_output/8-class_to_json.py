#!/usr/bin/python3

"""
This file contains a dict
"""
def class_to_json(obj):
    """
    This function return a dictionary description with simple data structure
    """
    vacio = {}
    for objeto in obj.__dict__:
        valor = obj.__dict__[objeto]
        if isinstance(valor, (list, dict, str, int, bool)):
            vacio[objeto] = valor

    return vacio
