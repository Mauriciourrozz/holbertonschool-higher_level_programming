#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary)
    for element in order:
        print(f"{element} : {a_dictionary[element]}")
