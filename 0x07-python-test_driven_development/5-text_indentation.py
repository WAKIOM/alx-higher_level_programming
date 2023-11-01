#!/usr/bin/python3
"""
module contains a function that splits lines based on .,?,:
"""


def text_indentation(text):
    """
    Split and print text into lines based on ".", "?",
    and ":" without using string methods.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = list(text)
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in (".", "?", ":"):
            if i + 1 < len(text) and text[i + 1] == " ":
                i += 1
            print('\n')
        i += 1
    print("\n")
