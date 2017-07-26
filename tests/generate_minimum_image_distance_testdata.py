#!/usr/bin/env python

import  MM_2017_SSS_Team2 as mm2
import numpy as np

test_input_coordinates = np.loadtxt('coordinates.txt', skiprows=2, usecols=(1, 2, 3))
box_length = 10
num_coordinates = len(test_input_coordinates)
testdata = []
for index0 in range(num_coordinates):
    for index1 in range(index0):
        coordinates0 = test_input_coordinates[index0, :]
        coordinates1 = test_input_coordinates[index1, :]
        output = mm2.minimum_image_distance.minimum_image_distance(coordinates0, coordinates1, box_length)
        testdata.append((coordinates0, coordinates1, box_length, output))

np.save("testdata_minimum_image_distance", testdata)
