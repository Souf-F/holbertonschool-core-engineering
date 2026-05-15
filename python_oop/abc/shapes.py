#!/usr/bin/env python3
"""
Shapes module - Abstract Shape class with concrete implementations
Demonstrates duck typing and polymorphism
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes

    Defines the interface that all shapes must implement
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape

        Returns:
            float: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape

        Returns:
            float: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class - concrete implementation of Shape

    Represents a circle defined by its radius
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius

        Args:
            radius (float): The radius of the circle
        """
        self.radius = abs(radius)  # ← Utilise valeur absolue

    def area(self):
        """
        Calculate the area of the circle

        Returns:
            float: Area = π × radius²
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle

        Returns:
            float: Perimeter = 2 × π × radius
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class - concrete implementation of Shape

    Represents a rectangle defined by its width and height
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with given width and height

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            float: Area = width × height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            float: Perimeter = 2 × (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing

    This function does not check the type of the object.
    It simply calls the area() and perimeter() methods,
    relying on the object to provide these methods.

    Args:
        shape: Any object that has area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
