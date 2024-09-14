#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    try:
        for i in range(x):
            if isinstance(i, int):
                print("{}".format(i), end="")
                cont += 1
        print()
    except IndexError:
        print()
    return cont
