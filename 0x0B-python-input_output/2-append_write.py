#!/usr/bin/python3

"""
The 2-append_write module
"""


def append_write(filename="", text=""):
    """
    append_write: appends a string at the end of a
    text file

    Attributes:
            filename: The file to append to
            text: The string to append
    """

    with open(filename, "a") as f:
        return f.write(text)
