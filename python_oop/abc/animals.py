#!/usr/bin/env python3
"""
Animals module - Abstract Animal class and concrete subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals

    Defines the contract that all animal subclasses must follow
    by requiring implementation of the sound method
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by all subclasses

        Returns:
            str: The sound the animal makes
        """
        pass


class Dog(Animal):
    """
    Dog class - concrete implementation of Animal

    Represents a dog that can make a barking sound
    """

    def sound(self):
        """
        Returns the sound a dog makes

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class - concrete implementation of Animal

    Represents a cat that can make a meowing sound
    """

    def sound(self):
        """
        Returns the sound a cat makes

        Returns:
            str: "Meow"
        """
        return "Meow"
