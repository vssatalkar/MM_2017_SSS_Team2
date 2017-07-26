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
