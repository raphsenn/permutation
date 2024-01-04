import pytest
from permutation.permutation import Permutation


def test_degree_1():
    p = Permutation()
    assert p.degree() == 1 # 0! = 1


def test_degree_2():
    p = Permutation(1)
    assert p.degree() == 1 # 1! = 1


def test_degree_3():
    p = Permutation(1, 2)
    assert p.degree() == 2 # 2! = 2 * 1 = 2


def test_degree_4():
    p = Permutation(1, 2, 3)
    assert p.degree() == 6 # 3! = 3 * 2 * 1 = 6


def test_degree_5():
    p = Permutation(1, 2, 3, 4)
    assert p.degree() == 24 # 4! = 4 * 3 * 2 * 1 = 24


def test_degree_6():
    p = Permutation(5, 1, 2, 4, 3)
    assert p.degree() == 120 # 5! = 5 * 4 * 3 * 2 * 1 = 120


def test_degree_7():
    p = Permutation(6, 5, 4, 3, 2, 1)
    assert p.degree() == 720 # 6! = 6 * 5! = 6 * 120 = 720
