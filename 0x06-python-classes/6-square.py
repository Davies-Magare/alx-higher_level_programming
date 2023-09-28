#!/usr/bin/python3
"""Module documentation
This module defines a square

"""


class Square:
    """This is a class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """position: retrieves the position attribute
        Return
        ______
        The position attribute

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position: sets the position attribute
        Parameters
        __________
        value: The position value passed
        Return
        ______
        The position attribute
        """
        if (value[0] < 0 or
            value[1] < 0 or
            len(position) != 2 or
                not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 "
                            "positive integers")
        self.__position = value

    @property
    def size(self):
        """size: getter method for size
        Parameters
        __________
        self: A reference to the object
        Returns
        _______
        The attribute i.e self.size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size: setter method for the size
        Parameters
        __________
        self: a reference to the object
        value: The value given by the user
        Returns
        _______
        Nothing

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area: Returns the area of a square
        Parameters
        __________
        size: The size of a side of the square

        Returns
        _______
        integer if Successful

        """
        return self.__size * self.__size

    def my_print(self):
        """my_print: Prints out the square with # to stdout
        Parameters
        __________
        self: a reference to the object

        Returns: Nothing
        """
        if (self.__size == 0):
            print()
            return
        for k in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for d in range(0, self.__position[0]):
                print(' ', end="")
            for j in range(0, self.__size):
                if j + 1 == self.size:
                    print('#')
                else:
                    print('#', end="")
