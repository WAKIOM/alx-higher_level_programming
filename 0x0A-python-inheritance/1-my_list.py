#!/usr/bin/python3
"""
Module contains one class
"""


class MyList(list):
    """
    Class inherits from 'list'
    Has one method
    """
    def print_sorted(self):
        """
        method returns a sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
