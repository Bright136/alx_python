"""
6-rectangle: Module for demonstrating inheritance and using super().

This module imports the BaseGeometry class from the numeric module named '5-base_geometry'.
It defines a Rectangle class that inherits from BaseGeometry and demonstrates the usage
of super() to call the parent class's methods.

Example:
    rectangle = Rectangle(10, 5)
"""

module_name = "5-base_geometry"  # Numeric module name
module = __import__(module_name).BaseGeometry

class Rectangle(module):
    """
    Rectangle class that inherits from BaseGeometry.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        
    Methods:
        __init__(width, height): Initializes the Rectangle with width and height.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with specified width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__() 
        self.__width = width
        self.__height = height
        self.integer_validator('height', self.__height)
        self.integer_validator('width', self.__width)






