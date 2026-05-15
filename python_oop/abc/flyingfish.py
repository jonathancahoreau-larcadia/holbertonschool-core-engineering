#!/usr/bin/env python3
"""
This module defines Fish, Bird, and FlyingFish classes
to demonstrate multiple inheritance and method overriding.
"""


class Fish:
    """
    Fish class representing aquatic animals.
    """
    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class representing flying animals.
    """
    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class demonstrating multiple inheritance from Fish and Bird.
    """
    def fly(self):
        """
        Print a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    """
    Demonstrate the behavior of the FlyingFish class.
    """
    flyingfish = FlyingFish()

    flyingfish.fly()
    flyingfish.swim()
    flyingfish.habitat()

    print(FlyingFish.mro())
