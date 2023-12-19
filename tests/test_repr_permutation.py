import pytest
from permutation.permutation import Permutation


def test_repr_1():
    p = Permutation(1)
    p.__repr__() == "()"


def test_repr_2():
    p = Permutation(1, 2)
    p.__repr__() == "()"


def test_repr_3():
    p = Permutation(1, 2, 3)
    p.__repr__() == "()"


def test_repr_4():
    p = Permutation(2, 1)
    p.__repr__() == "(1 2)"


def test_repr_5():
    p = Permutation(3, 2, 1)
    p.__repr__() == "(1 3)"


def test_repr_6():
    p = Permutation(5, 4, 1, 2, 6, 3, 7)
    p.__repr__() == "(1 5 6 3)(2 4)"


def test_repr_7():
    p = Permutation(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    p.__repr__() == "(1 10)(2 9)(3 8)(4 7)(5 6)"


def test_repr_8():
    p = Permutation(1, 2, 3, 4, 5, 6, 7, 8, 10, 9)
    p.__repr__() == "(9 10)"


def test_repr_9():
    p = Permutation(2, 1, 3, 4, 5, 6, 7, 8, 10, 9)
    p.__repr__() == "(1 2)(9 10)"
