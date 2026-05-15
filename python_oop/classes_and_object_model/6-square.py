#!/usr/bin/env python3
"""6-square.py: Square class with position and string representation."""


class Square:
    """Represent a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def my_print(self):
        """Print the square using the # character."""
        if self.size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.position[1]):
            print()

        line = " " * self.position[0] + "#" * self.size
        for _ in range(self.size):
            print(line)

    def __str__(self):
        """Return the string representation of
        the square (same as my_print)."""
        if self.size == 0:
            return ""

        lines = []
        # vertical offset
        for _ in range(self.position[1]):
            lines.append("")

        line = " " * self.position[0] + "#" * self.size
        for _ in range(self.size):
            lines.append(line)

        return "\n".join(lines)
