# Write a class Square that defines a square by: (based on 3-square.py)

# Private instance attribute: size:
# property def size(self): to retrieve it
# property setter def size(self, value): to set it:
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# Instantiation with optional size: def __init__(self, size=0):
# Public instance method: def area(self): that returns the current square area
# Public instance method: def my_print(self): that prints in stdout the square with the character #:
# if size is equal to 0, print an empty line
# You are not allowed to import any module


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


    def my_print(self):
        """
        Print a pattern of '#' characters.

        This method prints a pattern of '#' characters, where each row consists of a number of '#' characters
        equal to the value of the private attribute '__size'.

        Example:
            square = Square()
            square.size = 3
            square.my_print()
            # Output:
            # ###
            # ###
            # ###
        """
        if self.__size== 0:
            print()
        else:
            for num in range(self.__size):
                print(self.__size * '#')


