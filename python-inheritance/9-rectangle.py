#!/usr/bin/python3

'''Module for the class BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle inherits from BaseGeometry'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """this method returns the rectangle area"""
        return self.__height * self.__width

    def __str__(self):
        """This method returns the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
