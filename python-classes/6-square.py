#!/usr/bin/python3
'''This is a Square Module'''


class Square:
    '''this is a that defines a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''this is the constructeur'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''this a public methode to calculate the square area'''
        return self.__size ** 2

    def my_print(self):
        '''this module to print the square'''
        if self.__size == 0:
            print()
            return
        position_x = self.position[0] * " "
        position_y = self.position[1] * "\n"
        print(position_y, end='')
        for i in range(self.__size):
            print(position_x + "#" * self.__size)
