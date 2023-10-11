#!/usr/bin/python3
"""
The 6-load_from_json_file module
"""


def load_from_json_file(filename):
    """
    load_from_json_file: creates an object
    from a JSON file

    Attributes:
            filename: The file to convert
    """

    import json
    with open(filename, "r") as f:
        return json.load(filename)
