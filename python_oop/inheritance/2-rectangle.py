#!/usr/bin/env python3
"""
This module extends the Rectangle class with area
and string representation methods.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
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
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of rectangle.

        Returns:
            str: [Rectangle] width/height
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
