#!/usr/bin/env python3
"""
This module defines mixins and a Dragon class
to demonstrate multiple inheritance and method composition.
"""


class SwimMixin:
    """
    Mixin class to add swimming ability.
    """
    def swim(self):
        """
        Print a message indicating the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class to add flying ability.
    """
    def fly(self):
        """
        Print a message indicating the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class with swimming, flying, and roaring abilities.
    Inherits from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Print a message indicating the dragon roars.
        """
        print("The dragon roars!")


dragon = Dragon()

if __name__ == "__main__":
    """
    Demonstrate the behavior of the Dragon class.
    """
    dragon.swim()
    dragon.fly()
    dragon.roar()
