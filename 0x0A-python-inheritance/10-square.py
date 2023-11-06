#!/usr/bin/python3
"""
Square class module based on 9-rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle for representing squares.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with the size.

        Args:
        size (int): The size of the square.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: The string representation in the format "[Square] <size>/<size>".
        """
        return "[Rectangle] {}/{}".format(self._Rectangle__width,
                                          self._Rectangle__height)
