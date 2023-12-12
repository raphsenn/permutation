import pytest
from permutation.permutation import Permutation


def test_to_cycle_1():
    p = Permutation()
    assert p.to_cycle() == []


def test_to_cycle_2():
    p = Permutation(2, 1)
    assert p.to_cycle() == [(1, 2)]


def test_to_cycle_3():
    p = Permutation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert p.to_cycle() == []


def test_to_cycle_4():
    p = Permutation(2, 1, 3, 4, 5, 6, 7, 8, 9, 10)
    assert p.to_cycle() == [(1, 2)]


def test_to_cycle_5():
    p = Permutation(5, 4, 1, 2, 6, 3, 7)
    assert p.to_cycle() == [(1, 5, 6, 3), (2, 4)]


def test_to_cycle_6():
    p = Permutation(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert p.to_cycle() == [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)]
