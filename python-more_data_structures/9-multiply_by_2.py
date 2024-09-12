#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = {}
    for keyy, valor in a_dictionary.items():
        new_value = valor * 2
        new_dir[keyy] = new_value
    return new_dir
