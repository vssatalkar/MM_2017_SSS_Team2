"""
testing the math.py module.
"""

import MM_2017_SSS_Team2 as mm2
import pytest

def test_add():
    assert mm2.math.add(3, 4) == 7
    assert mm2.math.add(4, 4) == 8

testdata = [
    (2, 5, 10),
    (1, 2, 2),
    (3, 4, 12),
    (3, 3, 9),
    (6, 7, 42)
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult(a, b, expected):
    assert mm2.math.mult(a, b) == expected
    assert mm2.mult(b, a) == expected

def test_mod():
    assert mm2.math.mod(4, 3) == 1
    assert mm2.math.mod(6, 3) == 0

def test_power():
    assert mm2.math.power(4, 2) == 16
    assert mm2.power(2, 3) == 8

def test_min():
    assert mm2.math.min(2, 3) == 2
    assert mm2.math.min(3, 3) == 3

def test_max():
    assert mm2.math.max(3, 4) == 4
    assert mm2.math.max(4, 4) == 4

import numpy as np
import os
#box_length = 10.
#min_image_distance_testdata = [
#    (np.array([1., 1., 1.]), np.array([2., 2., 2.]), box_length, 3.),
#    (np.array([0., 0., 0.]), np.array([2., 2., 2.]), box_length, 12.),
#    (np.array([1., 1., 1.]), np.array([9., 9., 9.]), box_length, 12.)
#]
# r_i, r_j, box_length, minImageDist2
testdata_minimum_image_distance_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'testdata_minimum_image_distance.npy')
testdata_minimum_image_distance = np.load(testdata_minimum_image_distance_path)
@pytest.mark.parametrize("a,b,c,expected", testdata_minimum_image_distance)
def test_minimum_image_distance(a, b, c, expected):
    """
    Function to test the minimum image distance function in the source code
    """
    assert mm2.minimum_image_distance.minimum_image_distance(a, b, c) == expected
    return

testdata_rij = np.arange(0.5, 2, 0.5)
testdata_rij2 = testdata_rij**2
len_testdata_rij = len(testdata_rij)
testdata_lennard_jones = []
for i_data in range(len_testdata_rij):
	testdata_lennard_jones.append((testdata_rij2[i_data], mm2.minimum_image_distance.lennard_jones_potential(testdata_rij2[i_data])))

@pytest.mark.parametrize("a,expected", testdata_lennard_jones)
def test_lennard_jones(a, expected):
    """
    Function to test the lennard jones function in the source code;x
    """
    if a < 1.0:
        assert mm2.minimum_image_distance.lennard_jones_potential(a) > 0
    elif a == 1.0:
        assert mm2.minimum_image_distance.lennard_jones_potential(a) == 0
    else:
        assert mm2.minimum_image_distance.lennard_jones_potential(a) < 0
    return
