#!/usr/bin/python3
def no_c(my_string):
    str_sin_c = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            str_sin_c += char
    return str_sin_c
