#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    rev_list = list(reversed(my_list))
    for integer in rev_list:
        print("{:d}".format(integer))
