#!/usr/bin/env python3
"""
Module defining a square with position handling
and custom string representation.
"""


class Square:
    """Class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set square position."""
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # and position."""
        print(self.__str__())

    def __str__(self):
        """Return string representation of the square."""
        if self.__size == 0:
            return ""

        square = "\n" * self.__position[1]

        for i in range(self.__size):
            square += (" " * self.__position[0])
            square += "#" * self.__size

            if i != self.__size - 1:
                square += "\n"

        return square
