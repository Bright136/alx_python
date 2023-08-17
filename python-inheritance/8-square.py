"""
8-square - Module defining the Square class based on Rectangle inheritance.

This module imports the Rectangle class from the numeric module named '7-rectangle'.
It defines a Square class that inherits from Rectangle and demonstrates the usage
of inheritance to create a specialized square shape.

Example:
    s = Square(13)
    print(s)          # This will print the square description
    print(s.area())   # This will print the area of the square
"""

# Import the Rectangle class from the specified module
module_name = "7-rectangle"  # Numeric module name
module = __import__(module_name).Rectangle

class Square(module):
    """
    Square class that inherits from Rectangle.
    
    Attributes:
        None
        
    Methods:
        __init__(size): Initializes the Square with a given size.
    """
    def __init__(self, size):
        """
        Initialize a Square with a given size.
        
        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Get a string representation of the Square.
        
        Returns:
            str: A formatted string describing the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
