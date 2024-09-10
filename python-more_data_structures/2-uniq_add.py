#!/usr/bin/python3
def uniq_add(my_list=[]):
    vacio = []
    for i in my_list:
        if i not in vacio:
            vacio.append(i)
    suma = sum(vacio)
    return suma
