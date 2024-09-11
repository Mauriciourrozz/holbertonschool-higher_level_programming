#!/usr/bin/python3
def common_elements(set_1, set_2):
    vacio = []
    for i in set_1:
        for i in set_2:
            if i in set_1 and i in set_2:
                vacio.append(i)
            return vacio