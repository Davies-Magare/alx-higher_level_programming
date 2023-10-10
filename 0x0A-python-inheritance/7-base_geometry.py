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

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
