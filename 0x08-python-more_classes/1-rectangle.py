#!/usr/bin/python3
"""
This module describes an empty class
"""


class Rectangle:
    """Rectangle:Describes a rectangle
    This class describes a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width: retrieves the width of the rectangle
        Returns: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter: sets and validates the width of
        the rectangle
        Parameters
        __________
        value: The width of the rectangle passed
        Returns: The validated width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle
        Returns: The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """setter: sets and validates the height of the
        rectangle
        Parameters
        __________
        value: The height of the rectangle passed
        Returns: The validated height of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
