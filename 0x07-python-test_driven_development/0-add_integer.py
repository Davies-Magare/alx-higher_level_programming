#!/usr/bin/python3
"""
This is the "0_add_integer" module.

This module supplies one function, add_integer
"""


def add_integer(a, b=98):
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
