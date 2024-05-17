#!/usr/bin/python3
'''This is a Square Module'''


class Square:
    '''this is a that defines a square'''
    def __init__(self, size=0):
        '''this is the constructeur'''
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''this a public methode to calculate the square area'''
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
