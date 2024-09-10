#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for seccion in matrix:
        for num in seccion:
            if num == seccion[-1]:
                print("{:d}".format(num), end='')
            else:
                print("{:d}".format(num), end=" ")
        print()
