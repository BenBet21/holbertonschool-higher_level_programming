#!/usr/bin/python3
'''This is a Square Module'''


class Square:
    '''this is a that defines a square'''
    def __init__(self, size=0):
        '''this is the constructeur'''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''this a public methode to calculate the square area'''
        return self.__size ** 2
