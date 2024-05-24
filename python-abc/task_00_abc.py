#!/usr/bin/python3
"""this is an abstract class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """this Animal ABC"""
    @abstractmethod
    def sound(self):
        """ define sound method"""
        pass

class Dog(Animal):
    """this Dog Class inherits from Animal"""
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """this Cat Class inherits from Animal"""
    def sound(self):
        return ("Meow")
