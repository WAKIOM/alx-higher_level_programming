#!/usr/bin/python3
"""
Module contains one function
"""


def lookup(obj):
    """
    function takes one arg
    returns a list of attributes and objects
    """
    return f'{dir(obj)}'
