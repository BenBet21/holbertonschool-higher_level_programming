#!/usr/bin/python3

'''Module for the class Rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square inherits from Rectangle'''

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """this method returns the square area"""
        return self.__size ** 2
