#!/usr/bin/env python3
"""
Module 6-square
Définit une classe Square avec gestion de la position
et affichage personnalisé.
"""


class Square:
    """Classe représentant un carré avec gestion de la
        position et affichage personnalisé."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retourne la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré."""
        if type(value) is not tuple or len(value) != 2 or type(
            value[0]) is not int or type(value[1]) is not int or value[
                0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Affiche le carré avec la position donnée."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Retourne une représentation en chaîne du carré."""
        if self.__size == 0:
            return

        design = ""

        for _ in range(self.__position[1]):
            design += "\n"

        for _ in range(self.__size):
            design += " " * self.__position[0] + "#" * self.__size + "\n"
        return design.rstrip()
