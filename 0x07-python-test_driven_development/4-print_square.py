#!/usr/bin/python3
"""
This module contains the function print_square
"""


def print_square(size):
    """print_square: prints a square to stdout"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif not isinstance(size, int) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            if i + 1 == size:
                print('#')
            else:
                print('#', end="")
