#!/usr/bin/env python3
"""
This module defines an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to return the sound made by the animal.
        Must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Dog class, subclass of Animal.
    """

    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class, subclass of Animal.
    """

    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"
