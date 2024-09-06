#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    arg = argv[1:]
    suma = sum(int(ar) for ar in arg)
    print(suma)
