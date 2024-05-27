#!/usr/bin/python3
"""This function prints files contains"""


def read_file(filename=""):
    """0. Read file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
