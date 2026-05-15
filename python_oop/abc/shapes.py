#!/usr/bin/env python3
"""
Module defining abstract geometric shapes
using abstract base classes and duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize rectangle dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter using duck typing.

    Args:
        shape: Any object implementing
               area() and perimeter()
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
