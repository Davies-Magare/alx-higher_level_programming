#!/usr/bin/python3
"""
The 5-save_to_json_file module
"""


def save_to_json_file(my_obj, filename):

    """
    save_to_json_file - writes an object to
    a text file using JSON representation

    Attributes:
            my_obj: The object to write
            filename: The file to write to
    """
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
