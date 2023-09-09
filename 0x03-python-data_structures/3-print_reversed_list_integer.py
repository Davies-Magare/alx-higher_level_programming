#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    rev_list = reversed(my_list)
    for integer in rev_list:
        print("{:d}".format(integer))
