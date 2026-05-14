#!/usr/bin/env python3
"""
This module extends the Rectangle class with area
and string representation methods.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry
Rectangle = __import__('1-rectangle').Rectangle


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
