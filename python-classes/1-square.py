#!/usr/bin/python3
"""
1-square - A module for Sqaure .

This module provides classes for instantiating square objects.

"""

class Square:
    """
    Square - A class representing a square.

    This class defines a square with a private instance attribute for size.

    Attributes:
    __size (int): The size of the square's sides.

   
    Usage:
    square = Square(size=5)
    """

    def __init__(self, size=0):
        """
        Initialize a Square object with a given size.

        Args:
        size (int, optional): The size of the square's sides. Defaults to 0.
        """
        self.__size = size

        # Validate the size parameter.
        if type(size) != int:
            raise  TypeError('size must be an integer')
            # Raise a TypeError: If size is not an integer.
        elif size < 0:
            # Raise a ValueError: If size is negative.
            raise ValueError('size must be >= 0')







