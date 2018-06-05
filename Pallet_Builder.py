from Case import Case
from Layer import Layer
from Pallet import Pallet

"""Application to construct cases, layers, and pallets"""
case = Case()
case_data = []
for i in range(1, 3):
    for j in range(1, 3):
        case_data.append({'case': case, 'x': i, 'y': j, 'orient': 0})
layer = Layer(case_data)
Layer.contents(layer)
layer_data = []
for i in range(1, 3):
    layer_data.append({'layer': layer, 'orient': 0})

pallet = Pallet(layer_data)
pallet.contents()
