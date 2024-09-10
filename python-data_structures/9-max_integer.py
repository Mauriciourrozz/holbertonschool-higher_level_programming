#!/usr/bin/python3
def max_integer(my_list=[]):
    for num in my_list:
        maximo = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > maximo:
                maximo = my_list[i]  
        return maximo
