#!/usr/bin/python3
def no_c(my_string):
    str_list = list(my_string)
    i = 0
    while (i < len(str_list)):
        if str_list[i] == 'C':
            del(str_list[i])
        elif str_list[i] == 'c':
            del(str_list[i])
        i += 1
    new_str = ""
    for i in range(0, len(str_list)):
        new_str += str_list[i]
    return new_str
