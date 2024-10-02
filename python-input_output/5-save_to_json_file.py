#!/usr/bin/python3
"""
This file writes an object in text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object in text file in format JSON
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
