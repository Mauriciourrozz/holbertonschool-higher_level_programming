#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    nueva_lista = list(my_list)
    if idx < 0 and idx >= len(idx):
        return nueva_lista
    del my_list[idx]
    return my_list
