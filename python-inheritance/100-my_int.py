#!/usr/bin/python3

'''Module for the class MyInt'''


class MyInt(int):
    '''class MyInt inherits from int'''

    def __eq__(self, other):
        # Invert the behavior of ==
        return int(self) != other

    def __ne__(self, other):
        # Invert the behavior of !=
        return int(self) == other
