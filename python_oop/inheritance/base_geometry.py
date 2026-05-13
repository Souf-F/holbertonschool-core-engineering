#!/usr/bin/env python3
"""
BaseGeometry module
"""


class BaseGeometry:
    """Base class for geometric shapes"""

    def area(self):
        """
        Calculate area - not implemented in base class

        Raises:
            Exception: Always (must be implemented in subclasses)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is a positive integer

        Args:
            name (str): Name of the parameter
            value: Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
