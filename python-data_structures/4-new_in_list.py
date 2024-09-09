#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx >= len(my_list):
        return my_list
    nueva_lista = list(my_list)  # list() me duplica la lista
    nueva_lista[idx] = element
    return nueva_lista
