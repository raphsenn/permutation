import pytest
from permutation.permutation import Permutation


def test_cycle_to_permutation_1():
    p = Permutation()
    p.cycle([(1, 2, 3)])
    assert p.permutation == {1 : 2, 2 : 3, 3 : 1}
    assert p.__repr__() == "(1 2 3)"


def test_cycle_to_permutation_2():
    p = Permutation()
    p.cycle([(1, 5, 6, 3), (2, 4)])
    assert p.permutation == {1 : 5, 2 : 4, 3 : 1, 4 : 2, 5 : 6, 6 : 3}
    assert p.__repr__() == "(1 5 6 3)(2 4)"


def test_cycle_to_permutation_3():
    p = Permutation()
    p.cycle([(7, 6), (5, 4), (3, 2)])
    assert p.permutation == {1 : 1, 2 : 3, 3 : 2, 4 : 5, 5 : 4, 6 : 7, 7 : 6}
    assert p.__repr__() == "(2 3)(4 5)(6 7)"

def test_cycle_to_permutation_4():
    p = Permutation()
    p.cycle([(1, 2)])
    assert p.permutation == {1 : 2, 2 : 1}
    assert p.__repr__() == "(1 2)"
