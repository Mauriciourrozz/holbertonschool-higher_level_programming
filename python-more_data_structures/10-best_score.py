#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_max, value_max = list(a_dictionary.items())[0]
    for key, value in a_dictionary.items():
        if value > value_max:
            value_max = value
            key_max = key
    return key_max
