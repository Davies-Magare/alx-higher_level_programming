#!/usr/bin/python3
"""
This is the rectangle module
"""


class Rectangle:
    """ A class that describes a rectangle"""

    def __init__(self, width=0, height=0):
        """
        init: class constructor
        width: The width of the rectangle
        height: The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width: retrieves the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width: sets the width
        value: The value to set the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height: retrieves the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height: Validates and sets the height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
