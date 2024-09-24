#!/usr/bin/python3
"""
This file contains an object
"""



def is_same_class(obj, a_class):
    """
    This function return False if object is an instance of class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
