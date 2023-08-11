#!/usr/bin/python3

"""
0-is_kind_of_class.py - A module for checking whether an object is an 
instance of, or if the object is an instance of a class that inherited 
from, the specified class.

This module provides a function for checking .

"""
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

    This function takes an object and a class as arguments and determines
    whether the object is an instance of the specified class or an instance of a class 
    that inherited from, the specified class.

    Args:
        obj: Any Python object that you want to check.
        a_class: The class that you want to compare the object against.

    Returns:
        bool: Returns True if the object is an instance of the specified class or of an instance of a class that inherited from the specified class;
        otherwise, returns False.


    """
    return isinstance(obj, a_class)



