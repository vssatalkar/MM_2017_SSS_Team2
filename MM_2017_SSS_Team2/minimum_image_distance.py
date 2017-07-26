import numpy as np

def minimum_image_distance(r_i, r_j, box_length):
    """
    Function to compute minimum image distance between two particle coordinates for a given box length
    """
    rij = r_i - r_j 
    rij -= box_length * np.round(rij / box_length)
    rij2 = np.dot(rij, rij)
    return rij2
