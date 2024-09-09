#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nueva_lista = list(my_list)  # list() me duplica la lista
    if idx < 0 and idx >= len(my_list):
        return nueva_lista
    nueva_lista[idx] = element
    return nueva_lista
