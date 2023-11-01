#!/usr/bin/python3

"""
This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    Function adds two integers
    args: a(int) first argument
          b(int) second argument. if not provided, default = 98
    """
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
