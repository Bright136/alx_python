"""
8-square.py - Module defining the Square class based on Rectangle inheritance.

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
        self.integer_validator(value=size, name='size')


    def __str__(self):
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"




s = Square(13)

print(s)
print(s.area())
s = Square("13")

print(s)
print(s.area())