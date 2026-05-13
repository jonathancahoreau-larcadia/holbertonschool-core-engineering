#!/usr/bin/env python3
"""
Module 5-square
Définit une classe Square avec méthode my_print.
"""


class Square:
    """Classe représentant un carré avec méthode my_print."""
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

    def my_print(self):
        """Affiche le carré avec le caractère #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for row in range(self.__size):
                    print("{}".format("#"), end="")
                print()
