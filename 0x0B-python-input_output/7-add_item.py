#!/usr/bin/python3

"""
This script adds arguments to a python list
and saves them to a file
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    ls = load_from_json_file('add_item.json')
except FileNotFoundError:
    ls = []
i = 1
while i < len(sys.argv):
    ls.append(sys.argv[i])
    i += 1
save_to_json_file(ls, 'add_item.json')
