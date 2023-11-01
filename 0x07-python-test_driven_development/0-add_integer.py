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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a + b != int(a) + int(b):
        raise OverflowError("Result exceeds the\
                            maximum integer representable value")
    return a + b
