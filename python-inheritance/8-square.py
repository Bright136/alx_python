
module_name = "7-rectangle"  # Numeric module name
module = __import__(module_name).Rectangle


class Square(module):

    def __init__(self, size):
        super().__init__(size, size)

