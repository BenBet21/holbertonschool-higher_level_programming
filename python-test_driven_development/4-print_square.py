#!/usr/bin/python3
"""this is a print square # module"""


def print_square(size):
    """this function prints a square withe the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if isinstance(size,float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for nb in range(size):
            print("#", end='')
        print()
