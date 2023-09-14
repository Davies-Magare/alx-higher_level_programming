#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = list(a_dictionary)
    lst.sort()
    for item in lst:
        print("{}: {}".format(item, a_dictionary[item]))
