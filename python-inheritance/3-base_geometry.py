#!/usr/bin/python3
"""
3-base_geometry - A module for BaseGeometry .

This module provides classes for instantiating BaseGeometry.

"""
class BaseGeometry:
    """
        BaseGeometry - A class representing a basegeometry.

        This is an empty class with no attributes
    """
    def __dir__(self):
        """ Override the default behavior of the dir() function for the class.
            This method is called when the dir() function is used on an instance of the class.
            It filters out the '__init_subclass__' attribute from the list of attributes and methods
            returned by dir(), providing a customized view of the instance's attributes.
        """

        return [attr for attr in dir(self) if attr != '__init_subclass__']
    pass


