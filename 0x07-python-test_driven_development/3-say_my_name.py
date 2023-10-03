#!/usr/bin/python3
"""
This module defines the say_my_name function
"""

def say_my_name(first_name, last_name=""):
    """say_my_name: prints a person's first and last names
    Returns: Nothing
    """
    if isinstance(first_name, str) == False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) == False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
