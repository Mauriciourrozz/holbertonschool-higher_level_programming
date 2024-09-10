#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copia = []
    for num in my_list:
        if num % 2 == 0:
            copia.append(True)
        else:
            copia.append(False)
    return copia
