#!/usr/bin/python3

"""
The is_same module
"""


def is_same_class(obj, a_class):
    """
    is_same_class: checks whether an abject is the
    instance of a particular class
    Returns: True if the object is an instance of the
    class, Otherwise it returs false
    """
    if type(obj) == a_class:
        return True
    return False
