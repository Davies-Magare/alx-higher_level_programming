#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = []
    i = 0
    while (i < len(my_list)):
        cpy_list.append(my_list[i])
        i += 1
    if idx < 0:
        return cpy_list
    elif idx >= len(my_list):
        return cpy_list
    cpy_list[idx] = element
    return cpy_list
