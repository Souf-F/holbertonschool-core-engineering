#!/usr/bin/env python3
"""
Square module
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle

    A square is a special rectangle where width equals height

    Attributes:
        __size (int): Size of the square (private)
    """

    def __init__(self, size):
        """
        Initialize a new Square

        Args:
            size (int): Size of the square's side

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is <= 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
