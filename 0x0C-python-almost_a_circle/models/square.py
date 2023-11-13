#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square class that inherits from rect"""


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        size (int): Represents the size of the square.
        x (int): Represents the x-coordinate of the square.
        y (int): Represents the y-coordinate of the square.
        id (int): Represents the identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square.
            y (int): y-coordinate of the square.
            id (int): Identifier of the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: Formatted string representation.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, prop):
        """
        Setter method for the size attribute.

        Args:
            prop (int): The new size to set.

        Returns:
            None
        """
        self.width = prop
        self.height = prop

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes based on *args and **kwargs.

        If *args is present and not empty, it updates the attributes in order:
            - 1st argument: id
            - 2nd argument: size
            - 3rd argument: x
            - 4th argument: y

        If **kwargs is present,it updates attributes based on key-value pairs

        Args:
            *args: Variable length argument list.
            **kwargs: Variable length keyword argument list.

        Returns:
            None
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['id']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary representation of an object"""
        dct = {"id": self.id,
               "x": self.x,
               "size": self.size,
               "y": self.y}
        return dct
