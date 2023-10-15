#!/usr/bin/python3

"""The class_to_json module"""


def class_to_json(obj):
    """class_to_json - returns a serializable
    dictionary representation of an object
    """

    return obj.__dict__
