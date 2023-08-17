class CustomDirExample:
    def __init__(self):
        self.visible_attribute = 42
        self.hidden_attribute = "secret"

obj = CustomDirExample()

# Now, when you call dir() on the object, only 'visible_attribute' will be listed
print(dir(obj))

class FilteredCustomDirExample(CustomDirExample):
    def __dir__(self):
        return [attr for attr in dir(super()) if attr != '__init_subclass__']

# When you call dir() on the subclass, '__init_subclass__' will be excluded
print(dir(FilteredCustomDirExample))