#!/usr/bin/env python3
"""
Module 2-square
Définit une classe Square avec vérification du type et de la valeur de size.
"""


class Square:
    """Classe représentant un carré avec vérification
        du type et de la valeur de size."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
