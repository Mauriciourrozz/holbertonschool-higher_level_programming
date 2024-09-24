#!/usr/bin/python3
"""
This file contains an object
"""


def is_kind_of_class(obj, a_class):
    """
    This function return False if object is an instance of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
