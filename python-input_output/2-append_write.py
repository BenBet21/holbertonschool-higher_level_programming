#!/usr/bin/python3
"""This function appends a string at the end of a text \
file and returns the number of characters added:"""


def append_write(filename="", text=""):
    """2. Append to a file"""
    with open(filename, 'a', encoding="utf-8") as file:
        nb_characters = file.write(text)
        return nb_characters
