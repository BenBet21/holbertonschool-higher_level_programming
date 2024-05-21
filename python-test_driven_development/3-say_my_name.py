#!/usr/bin/python3
"""this i a print name module"""


def say_my_name(first_name, last_name=""):
    """this function prints My Name is"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
