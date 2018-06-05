"""class for defining a case on a pallet"""


class Case:
    def __init__(self, length=1, width=1, height=1, weight=1):
        """Initialize the default values for a case"""
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def dimensions(self):
        """Returns the dimensions and weight of the case"""
        return [self.length, self.width, self.height, self.weight]



