#!/usr/bin/python3
import json

"""
Module contains a function that returns the JSON
representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Function returns the JSON representation of a string
    args:
    my_obj: object to be converted
    returns:
    str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
