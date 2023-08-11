#!/usr/bin/python3

"""
0-is_same_class.py - A module for checking whether an object is a class of any kind .

This module provides a function so checking .

"""
def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    This function takes an object and a class as arguments and determines
    whether the object is an instance of the specified class.

    Args:
        obj: Any Python object that you want to check.
        a_class: The class that you want to compare the object against.

    Returns:
        bool: Returns True if the object is an instance of the specified class;
        otherwise, returns False.


    """
    return type(obj) is a_class



