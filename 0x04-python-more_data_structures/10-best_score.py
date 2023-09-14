#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    lst = list(a_dictionary)
    best = a_dictionary[lst[0]]
    for item in lst:
        if a_dictionary[item] > best:
            best = a_dictionary[item]
            ret = item
    return ret
