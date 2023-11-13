#!/usr/bin/python3
from models.base import Base
"""module contains a rectangle class that inherits from Base class"""


class Rectangle(Base):
    """A subclass of class Base.

    Class Rectangle inherits from Base.
    Private instance attributes, each with its own public getter and setter:

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the
        rectangle's position. Defaults to 0.
        y (int, optional): The y-coordinate of the
        rectangle's position. Defaults to 0.
        id (int, optional): The unique identifier of
        the rectangle. Defaults to None.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the
            rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
            rectangle's position. Defaults to 0.
            id (int, optional): The unique identifier
            of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """Retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, num: int) -> None:
        """Set and validate the width attribute.

        Args:
            num (int): The value to set as the width.

        Raises:
            TypeError: If num is not an integer.
            ValueError: If num is less than or equal to 0.
        """
        if type(num) is not int:
            raise TypeError("width must be an integer")
        if num <= 0:
            raise ValueError("width must be > 0")
        self.__width = num

    @property
    def height(self) -> int:
        """Retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, num: int) -> None:
        """Set and validate the height attribute.

        Args:
            num (int): The value to set as the height.

        Raises:
            TypeError: If num is not an integer.
            ValueError: If num is less than or equal to 0.
        """
        if type(num) is not int:
            raise TypeError("height must be an integer")
        if num <= 0:
            raise ValueError("height must be > 0")
        self.__height = num

    @property
    def x(self) -> int:
        """Retrieve the x attribute."""
        return self.__x

    @x.setter
    def x(self, num: int) -> None:
        """Set and validate the x attribute.

        Args:
            num (int): The value to set as the x coordinate.

        Raises:
            TypeError: If num is not an integer.
            ValueError: If num is less than 0.
        """
        if type(num) is not int:
            raise TypeError("x must be an integer")
        if num < 0:
            raise ValueError("x must be >= 0")
        self.__x = num

    @property
    def y(self) -> int:
        """Retrieve the y attribute."""
        return self.__y

    @y.setter
    def y(self, num: int) -> None:
        """Set and validate the y attribute.

        Args:
            num (int): The value to set as the y coordinate.

        Raises:
            TypeError: If num is not an integer.
            ValueError: If num is less than 0.
        """
        if type(num) is not int:
            raise TypeError("y must be an integer")
        if num < 0:
            raise ValueError("y must be >= 0")
        self.__y = num

    def area(self):
        """ return the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle by printing '#' chars

        The rectangle is positioned based on the values of `x` and `y`.
        The width and height of the rect are determined by `width` and `height`
        attributes.

        The '#' chars represent the filled area of the rectangle.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            string = ""
            for i in range(self.__width + self.__x):
                if i >= self.__x:
                    string += "#"
                else:
                    string += " "
            print(string)

    def __str__(self):
        """
        Override object string
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        The method accepts variable positional arguments and keyword arguments
        to update the rectangle's attributes, order of the arguments is assumed
        to be id, width, height, x, and y.
        """
        attribute_names = ['id', 'width', 'height', 'x', 'y']

        for i, value in enumerate(args):
            setattr(self, attribute_names[i], value)

        for name, value in kwargs.items():
            setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of an object"""
        dct = {"x": self.x,
               "y": self.y,
               "id": self.id,
               "width": self.width,
               "height": self.height}
        return dct
