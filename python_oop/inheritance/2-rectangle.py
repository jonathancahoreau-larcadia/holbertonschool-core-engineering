#!/usr/bin/env python3
"""
This module extends the Rectangle class with area
and string representation methods.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Represents a rectangle with width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """


    def area(self):
        return self.__width * self.__height


    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The string representation in the format [Rectangle] width/height.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
