#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False


def uppercase(str):
    i = 0
    while len(str) > i:
        if islower(str[i]):
            p = ord(str[i])
            p = p - 32
            p = chr(p)
        else:
            p = str[i]
        print("{}".format(p), end="")
        i += 1
    print()
