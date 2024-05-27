#!/usr/bin/python3
"""This function writes and returns number of characters written"""


def write_file(filename="", text=""):
    """1. Write to a file"""
    with open(filename, 'w', encoding="utf-8") as file:
        nb_characters = file.write(text)
        return nb_characters
