#!/usr/bin/python3
from models.base import Base
"""module contains a rectangle class that inherits from Base class"""


class Rectangle(Base):
    """A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new instance of the Rectangle class.

        getwidth(self):
            Gets the width of the rectangle.

        setweight(self, width):
            Sets the width of the rectangle.

        getheight(self):
            Gets the height of the rectangle.

        setheight(self, height):
            Sets the height of the rectangle.

        getx(self):
            Gets the x-coordinate of the rectangle.

        setx(self, x=0):
            Sets the x-coordinate of the rectangle.

        gety(self):
            Gets the y-coordinate of the rectangle.

        sety(self, y=0):
            Sets the y-coordinate of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def getwidth(self):
        """Get the width of the rectangle."""
        return self.__width

    def setweight(self, width):
        """Set the width of the rectangle."""
        self.__width = width

    def getheight(self):
        """Get the height of the rectangle."""
        return self.__height

    def setheight(self, height):
        """Set the height of the rectangle."""
        self.__height = height

    def getx(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    def setx(self, x=0):
        """Set the x-coordinate of the rectangle."""
        self.__x = x

    def gety(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    def sety(self, y=0):
        """Set the y-coordinate of the rectangle."""
        self.__y = y
