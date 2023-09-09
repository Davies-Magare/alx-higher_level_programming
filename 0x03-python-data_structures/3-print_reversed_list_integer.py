#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = reversed(my_list)
    for integer in rev_list:
        print("{}".format(integer))
