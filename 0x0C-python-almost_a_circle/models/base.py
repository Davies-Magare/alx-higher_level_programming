#!/usr/bin/python3

"""
The Base module
"""

import json


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file: saves list of instances to a file

        Attributes
        ==========
        list_objs: A list of class isntances to be serialized
        """
        class_name = type(list_objs[0]).__name__
        if list_objs is None or len(list_objs) == 0:
            dict_obj = []
        else:
            dict_obj = []
            for item in list_objs:
                if class_name == 'Rectangle':
                    dictnr = {
                            'id': item.id,
                            'width': item.width,
                            'height': item.height,
                            'x': item.x,
                            'y': item.y
                            }
                    dict_obj.append(dictnr)
                elif class_name == 'Square':
                    dictnr = {
                            'id': item.id,
                            'size': item.width,
                            'x': item.x,
                            'y': item.y
                            }
                    dict_obj.append(dictnr)
        json_str_obj = cls.to_json_string(dict_obj)
        filename = class_name + '.json'
        with open(filename, "w") as f:
            f.write(json_str_obj)
