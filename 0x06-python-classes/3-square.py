#!/usr/bin/python3
"""Module documentation
This module defines a square

"""


class Square:
    """This is a class that defines a square"""
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area: Returns the area of a square
        Parameters
        __________
        size
            The size of a side of the square
        Returns
        _______
        integer if Successful

        """
        return self.__size * self.__size
