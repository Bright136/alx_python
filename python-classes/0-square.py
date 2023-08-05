#!/usr/bin/python3

"""
0-square - A module for Sqaure .

This module provides classes for instantiating square objects .

"""
class Square:
    """

        Square - A class representing a square.

        This class defines a square with a private instance attribute for size.

        Attributes:
        __size : The size of the square's sides.

    """

    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Args:
        size : The size of the square's sides.
        """
        self.__size = size

   