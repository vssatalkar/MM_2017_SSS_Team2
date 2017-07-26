#!/usr/bin/env python

"""
This is a test for the lennard_jones_potential
"""

import numpy as np
#import matplotlib.pyplot as plt
#rij = (0)
#ri = []
#for ri in range (0, 10):
    # r2 = ri
rij = np.arange(0.1, 5, 0.5)
print(rij)
lj =np.zeros(len(rij))
#lj_potential_energy = []
#for a in range(0,len(rij)):
 #   rij2 = rij2.append(np.dot(rij[a] , rij[a]))
rij2 = rij*rij
#print (rij2)
#exit (-1)

def lennard_jones_potential(rij2):
    sig_by_r6 = (1 / rij2)**3
    sig_by_r12 = sig_by_r6**2
    potential_energy = 4.0 * (sig_by_r12 - sig_by_r6)
    return potential_energy
for i in range(0,len(rij2)):
    lj[i]=lennard_jones_potential(rij2[i])
    print(rij[i], lj[i])
#plt.plot(rij, lj)


