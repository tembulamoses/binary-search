# ============================================================================
# BinarySearch class implementation
# ============================================================================
class BinarySearch(list):
    """BinarySearch class
    This class sublcasses the builtin list class and extends it to have a search
    method that returns a dictionary {'count': int, 'index': int}
    The class __init__ method takes in the length and a step argument and populates
    itself based on their values
    it also has a length attribute that shows it length.
    """
    def __init__(self, a, b):
        """class constructor method"""

        # initialize the super class
        super(BinarySearch, self).__init__()

        # populate the class based on the length 
        # and step arguments
        for elem in range(1, a+1):
            self.append(elem * b)

        # define a length attribute
        self.length = len(self)