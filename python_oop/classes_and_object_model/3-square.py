#!/usr/bin/env python3
"""
Module 3-square
Définit une classe Square avec méthode area.
"""

class Square:
    """Classe représentant un carré avec méthode area."""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size
