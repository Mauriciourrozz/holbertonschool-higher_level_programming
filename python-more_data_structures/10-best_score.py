#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    valores = list(a_dictionary.values())
    max_value = valores [0]
    for valor in valores[1:]:
        if max_value < valor:
            max_value = valor
    return max_value
