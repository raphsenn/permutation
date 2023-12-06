import pytest
from permutation import Permutation


def test_order_1():
    p = Permutation()
    assert p.order() == 0


def test_order_2():
    p = Permutation(1)
    assert p.order() == 1


def test_order_3():
    p = Permutation(1, 2)
    assert p.order() == 2


def test_order_4():
    p = Permutation(1, 2, 3)
    assert p.order() == 6


def test_order_5():
    p = Permutation(1, 2, 3, 4)
    assert p.order() == 24

