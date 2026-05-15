#!/usr/bin/env python3
"""
Rectangle module
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry

    Attributes:
        __width (int): Width of the rectangle (private)
        __height (int): Height of the rectangle (private)
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
