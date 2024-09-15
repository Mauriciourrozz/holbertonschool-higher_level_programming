#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end='')
                count += 1
            elif isinstance(element, list):
                for j in element:
                    if isinstance(j, int):
                        print("{:d}".format(j), end='')
        print()
    except TypeError:
        print()
    return count
