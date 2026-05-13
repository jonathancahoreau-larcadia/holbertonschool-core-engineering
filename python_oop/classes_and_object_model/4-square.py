#!/usr/bin/env python3
"""
Module 4-square
Définit une classe Square avec accesseurs et mutateurs pour size.
"""


class Square:
    """Classe représentant un carré avec accesseurs et mutateurs pour size."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré."""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size
