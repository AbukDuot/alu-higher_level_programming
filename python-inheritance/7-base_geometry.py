#!/usr/bin/python3
"""defines BaseGeometry class
with public instance methods for area integer validation"""


class BaseGeometry:
    """class with public method to raise exception
    and public instance method to validate integer"""
    def area(self):
        """raises exception that area method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
