"""
4-base_geometry.py - Module defining the BaseGeometry class with area() method.

This module contains the definition of the BaseGeometry class, which serves as a base class
for geometry-related classes. The BaseGeometry class provides an area() method that raises
an Exception indicating that the method is not implemented.

Example:
    bg = BaseGeometry()
    try:
        area = bg.area()  # This will raise an Exception
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

"""

class BaseGeometry:
    """
    BaseGeometry class provides a foundation for geometry-related classes.
    
    Attributes:
        None
        
    Methods:
        area(): Raises an Exception indicating that the method is not implemented.
    """
    def area(self):
        """
        Calculate the area of the geometry.
        
        This method is intended to be overridden by subclasses to provide a valid area calculation.
        
        Raises:
            Exception: Indicates that the area() method is not implemented.
        
        Returns:
            None
        """
        raise Exception("area() is not implemented")



# if __name__ == "__main__":
#     bg = BaseGeometry()
#     try:
#         print(bg.area())
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
