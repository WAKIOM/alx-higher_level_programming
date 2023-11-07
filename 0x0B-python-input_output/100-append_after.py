#!/usr/bin/python3
"""
Insert a line of text into a file after each line containing a specific string.

"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text into a file after each line
    containing a specific string.

    Args:
    filename (str): The name of the file to be processed.
    search_string (str): The string to search for in each line of the file.
    new_string (str): The line of text to insert after line with search string.

    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
