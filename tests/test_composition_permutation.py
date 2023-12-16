import pytest
from permutation.permutation import Permutation


def test_composition_1():
    p = Permutation(1, 3, 2)
    q = Permutation(3, 2, 1)
    assert (p*q).permutation == {1 : 2, 2 : 3, 3 : 1}


def test_composition_2():
    p = Permutation(1, 3, 2)
    q = Permutation(3, 2, 1)
    assert (q * p).permutation == {1 : 3, 2 : 1, 3 : 2}


def test_composition_3():
    p = Permutation(1, 3, 2)
    q = Permutation(3, 2, 1)
    assert (p*q).permutation != (q*p).permutation
