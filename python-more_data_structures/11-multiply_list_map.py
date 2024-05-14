#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):

    if not my_list:
        return None

    new_list = list(map(lambda x: x * number, my_list))

    return new_list
