#!/usr/bin/python3


"""
0-2-inherits_from - A module checks if the class of an instance is inherited from a specified base class.

This module provides a function for checking.

"""

def inherits_from(obj, a_class):
    """
    Check if the class of an instance is inherited from a specified base class.

    This function takes an instance and a base class as arguments and determines
    whether the class of the instance is a subclass of the specified base class.

    Args:
        instance: An instance of any class that you want to check.
        base_class: The base class that you want to check against.

    Returns:
        bool: Returns True if the class of the instance is a subclass of the specified base class;
        otherwise, returns False.

    Example:
        class Animal:
            pass

        class Dog(Animal):
            pass

        class Cat(Animal):
            pass

        my_dog = Dog()
        my_cat = Cat()

        is_dog_animal = is_subclass(my_dog, Animal)  # Returns True
        is_cat_animal = is_subclass(my_cat, Animal)   # Returns True
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

