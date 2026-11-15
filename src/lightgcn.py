import numpy as np

def propagate_one_layer(P, E0):
    E1 = P @ E0
    return E1
