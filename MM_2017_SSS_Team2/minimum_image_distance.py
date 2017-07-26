import numpy as np

def minimum_image_distance(r_i, r_j, box_length):
    """
    Function to compute minimum image distance between two particle coordinates for a given box length
    """
    rij = r_i - r_j 
    rij -= box_length * np.round(rij / box_length)
    rij2 = np.dot(rij, rij)
    return rij2

def lennard_jones_potential(rij2):
    """
    Function to compute Lennard Jones potential for a given squared distance 
    """
    sig_by_r6 = (1 / rij2)**3
    sig_by_r12 = sig_by_r6**2
    potential_energy = 4.0 * (sig_by_r12 - sig_by_r6)
    return potential_energy

