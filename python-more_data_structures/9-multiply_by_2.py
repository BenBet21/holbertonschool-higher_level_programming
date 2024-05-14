#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    mul_dict = {}

    for key, value in a_dictionary.items():
        mult_value = value * 2
        mul_dict[key] = mult_value

    return mul_dict
