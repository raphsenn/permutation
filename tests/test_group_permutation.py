import pytest
from permutation.permutation import Permutation


def test_group_1():
    assert Permutation.group(1) == [Permutation(1)]


def test_group_2():
    assert Permutation.group(2) == [Permutation(1, 2), Permutation(2, 1)]
