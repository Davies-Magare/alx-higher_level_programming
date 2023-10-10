#!/usr/bin/python3

"""
The read file module
"""


def read_file(filename="", text=""):
    """write file: reads a file and prints
    it to stdout

    Args:
        filename: The nname of the file
    """

    with open(filename, encoding="utf-8") as f:
        txt_read = f.read()
    print(txt_read, end="")
