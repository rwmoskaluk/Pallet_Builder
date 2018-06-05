"""Class for defining and grouping a layer of cases"""


class Layer:
    def __init__(self, layer):
        """
            Initializes the layer with associated cases
            layer: [[case1, x, y, orient], [case2, x, y, orient]]
            case: [length, width, height, weight]

        """
        self.layer = layer

    def contents(self):
        """returns the contents of the layer"""
        for i in range(0, len(self.layer)):
            print('case{0} = [length = {1} width = {2} '
                  'height = {3} weight = {4} x = {5} y = {6} orient = {7}]'
                  .format(i+1,
                          self.layer[i]['case'].length,
                          self.layer[i]['case'].width,
                          self.layer[i]['case'].height,
                          self.layer[i]['case'].weight,
                          self.layer[i]['x'],
                          self.layer[i]['y'],
                          self.layer[i]['orient']))

    def set_case_location(self, case_num, x, y):
        """Sets a specific case's location"""
        self.layer[case_num]['x'] = x
        self.layer[case_num]['y'] = y

    def set_case_orientation(self, case_num, orient):
        """Sets a specific case's orientation"""
        self.layer[case_num]['orient'] = orient

    def check_uniqueness(self):
        """Method for checking that each case resides in a unique location"""
        for i in range(0, len(self.layer)):
            pass
