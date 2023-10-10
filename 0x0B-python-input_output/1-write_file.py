#!/usr/bin/python3

"""
The write_file module
"""


def write_file(filename="", text=""):
    """
    write_file: writes a string to a textfile

    Args:
        filename: The file to write to
        text: The string to write to the file
    """

    with open(filename, "w") as f:
        return f.write(text)
