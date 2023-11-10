#!/usr/bin/python3
"""Module contains base class"""


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
