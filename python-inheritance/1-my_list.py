#!/usr/bin/python3
"""this is a module that write a class that inherits from list"""


class MyList(list):
    """this class inherits from list"""
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
        return new_list
