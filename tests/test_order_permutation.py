import pytest
from permutation.permutation import Permutation


def test_order_1():
    p = Permutation()
    assert p.order() == 1 # 0! = 1


def test_order_2():
    p = Permutation(1)
    assert p.order() == 1 # 1! = 1


def test_order_3():
    p = Permutation(1, 2)
    assert p.order() == 2 # 2! = 2 * 1 = 2


def test_order_4():
    p = Permutation(1, 2, 3)
    assert p.order() == 6 # 3! = 3 * 2 * 1 = 6


def test_order_5():
    p = Permutation(1, 2, 3, 4)
    assert p.order() == 24 # 4! = 4 * 3 * 2 * 1 = 24


def test_order_6():
    p = Permutation(5, 1, 2, 4, 3)
    assert p.order() == 120 # 5! = 5 * 4 * 3 * 2 * 1 = 120


def test_order_7():
    p = Permutation(6, 5, 4, 3, 2, 1)
    assert p.order() == 720 # 6! = 6 * 5! = 6 * 120 = 720
