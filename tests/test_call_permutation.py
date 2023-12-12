import pytest
from permutation.permutation import Permutation
from extra.random_permutation import generate_random_permutation


def test_call_permutation_1():
    p = Permutation(1)
    assert p(1) == 1


def test_call_permutation_2():
    p = Permutation(3, 2, 1)
    assert p(1) == 3
    assert p(2) == 2
    assert p(3) == 1


def test_call_permutation_3():
    p = Permutation(5, 3, 1, 2, 4)
    assert p(1) == 5
    assert p(2) == 3
    assert p(3) == 1
    assert p(4) == 2
    assert p(5) == 4
