#!/usr/bin/python3
"""
This file serializes and deserializes an object
"""


import json
import os


def serialize_and_save_to_file(data, filename):
    """
    This function serializes a file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    This function deserializes a file
    """
    with open(filename, 'r', encoding='utf=8') as file:
        return json.load(file)
