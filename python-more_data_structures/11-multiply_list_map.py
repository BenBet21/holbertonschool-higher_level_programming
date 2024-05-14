#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):

    if not my_list:
        return None

    new_list = []
    len(new_list) == len(my_list)

    mul_val = 0
    for value in my_list:
        mul_val = value * number
        new_list.append(mul_val)
    return new_list
