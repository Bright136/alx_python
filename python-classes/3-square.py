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

   
    Methods:
    __init__(size=0): Initialize a Square object with a given size.
    area(): Calculate the area of the square.

    Usage:
    square = Square(size=5)
    area = square.area()
    square.size # return the size 
    """

    def __init__(self, size=0):
        """
        Initialize a Square object with a given size.

        Args:
        size (int, optional): The size of the square's sides. Defaults to 0.
        """
        self.__size = size
    

    @property
    def size(self):
        """
        Get the current size value.

        Returns:
            int: The current size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size value after validating it.

        Args:
            value (int): The new size value to be set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is negative.

        Example:
            square = Square()
            square.size = 10  # Sets the size to 10.
        """
        # Validate the size parameter.
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2





