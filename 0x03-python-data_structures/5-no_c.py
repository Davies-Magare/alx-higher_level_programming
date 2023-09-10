#!/usr/bin/python3
def no_c(my_string):
    if my_string == "":
        return my_string
    str_ret = ""
    for item in my_string:
        if item != 'C' and item != 'c':
            str_ret += item
    return str_ret
