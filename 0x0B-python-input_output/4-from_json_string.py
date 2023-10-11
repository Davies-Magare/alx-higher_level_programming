#!/usr/bin/python3
"""
The 4-from_json_string module
"""


def from_json_string(my_str):
    """
    from_json_string: returns the object represented
    by a JSON string

    Attributes:
            my_str: Object to convert from JSON format
    """
    import json

    return json.loads(my_str)
