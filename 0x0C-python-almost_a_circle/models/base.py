#!/usr/bin/python3
"""Module contains base class"""
import json


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiating the class"""
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.__nb_objects = self.id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        st = json.dumps(list_dictionaries)
        return st

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None:
            return []
        return json.loads(json_string)
