import pytest
from permutation.permutation import Permutation
from extra.random_permutation import generate_random_permutation


def test_eq_permutation_1():
    p = Permutation(1)
    q = Permutation(1)
    assert p == p
    assert p == q


def test_eq_permutation_2():
    p = Permutation(1, 2, 3)
    q = Permutation(3, 2, 1)
    assert p * q == q * p


def test_eq_permutation_3():
    p = Permutation(2, 3, 1)
    q = Permutation(3, 1, 2)
    id_ = Permutation(1, 2, 3)
    assert p * q == id_
    assert q * p == id_
    assert p * q == q * p


@pytest.mark.parametrize("permutation_input", [
    generate_random_permutation(100) for _ in range(100)
])
def test_eq_permutation_100(permutation_input):
    p = Permutation(*permutation_input)
    q = Permutation(*permutation_input)
    assert p == q
