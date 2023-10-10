#!/usr/bin/python3

"""
The BaseGeometry module
"""


class BaseGeometry:
    """The BaseGeometry class"""

    pass

    def area(self):
        """area: raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator: validates value
        name: A name
        value: An integer
        """

        if not isinstance(value, int) or value is True:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """The rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
