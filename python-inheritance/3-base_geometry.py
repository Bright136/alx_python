#!/usr/bin/python3

"""

3-base_geometry - A module for BaseGeometry .

This module provides classes for instantiating BaseGeometry.

"""
#!/usr/bin/python3

class CustomDirMeta(type):
    """
    CustomDirMeta - A metaclass for customizing the dir() behavior.

    This metaclass is used to customize the list of attributes and methods shown
    for classes that inherit from it.

    """

    def __dir__(cls):
        """
        __dir__ - Customize the list of attributes and methods shown for the class.

        This method is called when the dir() function is used on a class. It modifies
        the list of attributes and methods returned by dir() to exclude the
        '__init_subclass__' attribute.

        :return: A filtered list of attributes and methods for the class.
        :rtype: list
        """
        dir_list = super().__dir__()
        dir_list.remove('__init_subclass__')
        return dir_list

"""
3-base_geometry - A module for BaseGeometry.

This module provides classes for instantiating BaseGeometry.
"""

class BaseGeometry(metaclass=CustomDirMeta):
    """
    BaseGeometry - A class representing a base geometry.

    This is an empty class with no attributes.

    """

    def __dir__(self):
        """
        __dir__ - Override the default behavior of the dir() function for the class.

        This method is called when the dir() function is used on an instance of the class.
        It filters out the '__init_subclass__' attribute from the list of attributes and methods
        returned by dir(), providing a customized view of the instance's attributes.

        :return: A filtered list of attributes and methods for the instance.
        :rtype: list
        """
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
