module_name = "5-base_geometry"  # Numeric module name
module = __import__(module_name).BaseGeometry



class Rectangle(module):
    
    def __init__(self, width, height):
        super().__init__() 
        self.__width = width
        self.__height = height
        self.integer_validator('height', self.__height)
        self.integer_validator('width', self.__width)



# Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

# Instantiation with width and height: def __init__(self, width, height):
# width and height must be private. No getter or setter
# width and height must be positive integers, validated by integer_validator


r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))