#!/usr/bin/python3
for a in range(9):
    for b in range(a + 1, 10):
        if a == 8 and 9 == 9:
            print("{}{}".format(a,b))
        elif a != b:
            print("{}{}".format(a, b), end=', ')
