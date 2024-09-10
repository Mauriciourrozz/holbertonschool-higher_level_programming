#!/usr/bin/python3
def search_replace(my_list, search, replace):
    vacia = []
    for i in my_list:
        if i == search:
            vacia.append(replace)
        else:
            vacia.append(i)
    return vacia
