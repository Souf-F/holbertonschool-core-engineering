#!/usr/bin/env python3
"""
Dragon module - Demonstrates the use of mixins for composable behaviors
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability

    This mixin can be added to any class to give it the ability to swim
    """

    def swim(self):
        """
        Method that describes swimming behavior
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability

    This mixin can be added to any class to give it the ability to fly
    """

    def fly(self):
        """
        Method that describes flying behavior
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines swimming and flying abilities using mixins

    Inherits from SwimMixin and FlyMixin to gain swim() and fly() methods
    """

    def roar(self):
        """
        Method specific to Dragon that describes roaring behavior
        """
        print("The dragon roars!")
