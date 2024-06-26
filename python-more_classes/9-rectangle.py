#!/usr/bin/python3
'''This is Rectangle Module'''


class Rectangle:
    '''this is a class Rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''this is the constructeur'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''this is public method to return rectangle area'''
        return self.__height * self.__width

    def perimeter(self):
        '''this is public method to return rectangle perimeter'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        rect_lines = []
        for i in range(self.height):
            rect_lines.append(str(self.print_symbol) * self.width)
        return "\n".join(rect_lines)

    def __repr__(self):
        '''return a string that represents the rectangle'''
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        '''to delete an instance of Rectangle'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''to return a new rectangle with width == height == size'''
        return cls(size, size)
