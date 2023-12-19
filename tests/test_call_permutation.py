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


def test_call_permutation_4():
    p = Permutation(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert p(1) == 1
    assert p(2) == 2
    assert p(3) == 3
    assert p(4) == 4
    assert p(5) == 5
    assert p(6) == 6
    assert p(7) == 7
    assert p(8) == 8
    assert p(9) == 9
    assert p(10) == 10


def test_call_permutation_5():
    p = Permutation(1, 2, 3, 4, 5, 6, 7, 10, 9, 8)
    assert p(1) == 1
    assert p(2) == 2
    assert p(3) == 3
    assert p(4) == 4
    assert p(5) == 5
    assert p(6) == 6
    assert p(7) == 7
    assert p(8) == 10
    assert p(9) == 9
    assert p(10) == 8


@pytest.mark.parametrize("permutation_input", [
    generate_random_permutation(100) for _ in range(100)
])
def test_call_permutation_50(permutation_input):
    p = Permutation(*permutation_input)
    for i in range(1, 101):
        assert p(i) == permutation_input[i - 1]




