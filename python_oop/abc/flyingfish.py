#!/usr/bin/env python3
"""
FlyingFish module - Demonstrates multiple inheritance and MRO
"""


class Fish:
    """
    Fish class - represents aquatic animals
    """

    def swim(self):
        """
        Method describing fish swimming behavior
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method describing fish habitat
        """
        print("The fish lives in water")


class Bird:
    """
    Bird class - represents flying animals
    """

    def fly(self):
        """
        Method describing bird flying behavior
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method describing bird habitat
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class - inherits from both Fish and Bird

    Demonstrates multiple inheritance by combining behaviors
    from both parent classes and overriding methods
    """

    def fly(self):
        """
        Override Bird's fly method with FlyingFish specific behavior
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override Fish's swim method with FlyingFish specific behavior
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override habitat method from both parents
        """
        print("The flying fish lives both in water and the sky!")
