import pytest
from permutation.permutation import Permutation


def test_get_group_1():
    p = Permutation(1)
    assert p.get_group() == [[()]]


def test_get_group_2():
    p = Permutation(1, 2)
    assert p.get_group() == [[()], [(1, 2)]]


def test_get_group_3():
    p = Permutation(1, 2 ,3)
    assert p.get_group() == [[()], [(1, 2)], [(1, 3, 2)], [(2, 3)], [(1, 2, 3)], [(1, 3)]]


def test_get_group_4():
    p = Permutation(4, 1, 3, 2)
    assert len(p.get_group()) == 24


def test_get_group_5():
    p = Permutation(5, 4, 3, 2, 1)
    assert len(p.get_group()) == 120


def test_get_group_6():
    p = Permutation(3, 1, 2, 4, 6, 5)
    assert len(p.get_group()) == 720
