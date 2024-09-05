#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    elif len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))

    count = 1
    for elem, argv in enumerate(argv[1:]):
        count += 1
        print("{}: {}".format(count - 1, argv))
