#!/usr/bin/python3
"""
This file contains an object
"""


def inherits_from(obj, a_class):
    """
    This function return True if the object is an instance of class
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
