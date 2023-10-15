#!/usr/bin/python3

"""
The student module
"""


class Student:
    """The student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - returns a dictionary representation of an
        instance of class Student
        """
        result = {}
        if attrs is None:
            return self.__dict__
        for item in attrs:
            if hasattr(self, item):
                result[item] = getattr(self, item)
        return result
