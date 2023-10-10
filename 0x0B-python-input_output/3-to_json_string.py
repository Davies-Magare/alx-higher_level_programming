#!/usr/bin/python3

"""
The 3-to_json_string module
"""


def to_json_string(my_obj):
    """
    to_json_string -returns the JSON representation
    of an object(string)

    Attributes:
            my_obj: The object
    """
    import json
    return json.dumps(my_obj)
