#!/usr/bin/python3

"""
This module describes class MyList
"""


class MyList(list):

    """The class MyList"""

    def append(self, member):
        """append: appends new members to the list"""

        super().append(member)

    def print_sorted(self):
        """print_sorted: returns a sorted list"""
        sortd = sorted(self)
        print(sortd)
