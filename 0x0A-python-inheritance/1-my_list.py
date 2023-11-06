#!/usr/bin/python3
"""
Module contains one class
"""


class MyList(list):
    """
    Class inherits from 'list'
    Has one method
    """
    def __init__(self):
        """ initialize the object"""
        super().__init__()

    def print_sorted(self):
        """
        method returns a sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
