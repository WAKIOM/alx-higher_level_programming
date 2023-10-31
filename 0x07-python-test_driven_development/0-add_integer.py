#!/usr/bin/python3

"""
This module contains a function that adds two integers
a: first argument
b: second argument
"""


def add_integer(a, b=98):
    """
    Function adds two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a, b = int(a), int(b)
    return a + b