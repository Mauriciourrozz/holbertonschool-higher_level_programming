#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    sum_ab = add(a, b)
    res_ab = sub(a, b)
    mul_ab = mul(a, b)
    div_ab = div(a, b)
    print("{} + {} = {}".format(a, b, sum_ab))
    print("{} - {} = {}".format(a, b, res_ab))
    print("{} * {} = {}".format(a, b, mul_ab))
    print("{} / {} = {}".format(a, b, div_ab))
