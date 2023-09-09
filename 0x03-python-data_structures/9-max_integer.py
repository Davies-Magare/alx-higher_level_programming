#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    i = 0
    biggest = my_list[i]
    i += 1
    while i < len(my_list):
        if my_list[i] > biggest:
            biggest = my_list[i]
        i += 1
        return biggest


