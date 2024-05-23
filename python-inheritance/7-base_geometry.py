#!/usr/bin/python3
'''This is Geometry Module'''


class BaseGeometry:
    '''this is a class BaseGeometry'''

    def area(self):
        """this method raise execption"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method validates value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True
