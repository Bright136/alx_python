class Base:
    """
    Represents a base class with a private class attribute and a constructor.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the number of instances created.

    Methods:
        __init__(self, id=None):
            Initializes a new instance of the Base class.
            Args:
                id (int or None): An optional identifier for the instance. If provided, assigns the id to the instance.
                                 If not provided, increments the __nb_objects counter and assigns the counter value to the instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        
        Args:
            id (int or None): An optional identifier for the instance. If provided, assigns the id to the instance.
                             If not provided, increments the __nb_objects counter and assigns the counter value to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
