#!/usr/bin/python3
"""this is an abstract class"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """this Shape ABC"""

    @abstractmethod
    def area(self):
        """ define area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """ define perimeter method"""
        pass


class Circle(Shape):
    """this Circle Class inherits from Shape"""

    def __init__(self, radius):
        '''this is the constructeur'''
        self.radius = radius

    def area(self):
        '''this is public method to return circle area'''
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        '''this is public method to return circle area'''
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """this Rectangle Class inherits from Shape"""

    def __init__(self, width, height):
        '''this is the constructeur'''
        self.width = width
        self.height = height

    def area(self):
        '''this is public method to return rectangle area'''
        return self.width * self.height

    def perimeter(self):
        '''this is public method to return rectangle perimeter'''
        return (self.width + self.height) * 2


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
