"""Class for defining a pallet of layers made up of cases"""


class Pallet:
    def __init__(self, pallet):
        """
            Initializes the pallet with specific layers
            pallet: [[layer1, orient], [layer2, orient]]
            layer: [[case1, x, y, orient], [case2, x, y, orient]]
            case: [length, width, height, weight]
        """

        self.pallet = pallet

    def contents(self):
        """Returns the contents of the pallet"""
        for i in range(0, len(self.pallet)):
            my_string = 'layer{0} = ['
            print(my_string.format(i+1))
            for j in range(0, len(self.pallet[i]['layer'].layer)):
                print('\t\tcase{0} = [length = {1} width = {2} '
                      'height = {3} weight = {4} x = {5} y = {6} orient = {7}]'
                      .format(j+1,
                              self.pallet[i]['layer'].layer[j]['case'].length,
                              self.pallet[i]['layer'].layer[j]['case'].width,
                              self.pallet[i]['layer'].layer[j]['case'].height,
                              self.pallet[i]['layer'].layer[j]['case'].weight,
                              self.pallet[i]['layer'].layer[j]['x'],
                              self.pallet[i]['layer'].layer[j]['y'],
                              self.pallet[i]['layer'].layer[j]['orient']))
            print('\t\t ]')

    def swap_layers(self, layer_1, layer_2):
        """Method for swapping layer locations on the pallet"""
        if len(self.pallet) >= 2:
            self.pallet[layer_1], self.pallet[layer_2] = self.pallet[layer_2], self.pallet[layer_1]
