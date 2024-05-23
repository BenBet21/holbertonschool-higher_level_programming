#!/usr/bin/python3

"""this function returns true if the \
object is exactly an instance of the \
specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """this method return true if the \
object is exactly an instance of the \
specified class"""

    return type(obj) is a_class
