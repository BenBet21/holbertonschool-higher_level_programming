#!/usr/bin/python3

def max_integer(my_list=[]):

    Max = my_list[0]

    if len(my_list) == 0:
        return None

    for item in my_list:
        if item > Max:
            Max = item

    return Max
