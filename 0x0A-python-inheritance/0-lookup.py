#!/usr/bin/python3
"""
This module returns the avaialbe attributes and methods
of an object
"""


def lookup(obj):
    """lookup: lookup function"""
    return list(dir(obj))
