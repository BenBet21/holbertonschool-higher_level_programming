#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    for index, element in enumerate(my_list):
        if printed_elements < x:
            try:
                print(element, end='')
                printed_elements += 1
            except TypeError:
                pass
    print()
    return printed_elements
