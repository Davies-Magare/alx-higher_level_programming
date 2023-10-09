#!/usr/bin/python3

"""
The is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class: checks whether an object is an instance of
    a class or its subclass
    Returns: True if it is the case, otherwise False is returned
    """

    if isinstance(obj, a_class) is True:
        return True
    return False
