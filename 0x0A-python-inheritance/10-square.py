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

    def area(self):
        """The area method"""

        return self.__width * self.__height

    def __str__(self):
        """returns string representation of rectangle"""

        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        The area method
        Returns: The area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""

        return '[Rectangle] {}/{}'.format(self.__size, self.__size)
