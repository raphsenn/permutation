import pytest
from permutation.permutation import Permutation
from extra.random_permutation import generate_random_permutation


def test_is_abelian_1():
    p = Permutation()
    assert p.is_abelian() == False


def test_is_abelian_2():
    p = Permutation(1)
    assert p.is_abelian() == True


def test_is_abelian_3():
    p = Permutation(1, 2)
    assert p.is_abelian() == True


def test_is_abelian_4():
    p = Permutation(1, 2, 3)
    assert p.is_abelian() == False


def test_is_abelian_5():
    p = Permutation(1, 2, 3, 4)
    assert p.is_abelian() == False


def test_is_abelian_6():
    p = Permutation(1, 2, 3, 4, 5)
    assert p.is_abelian() == False


def test_is_abelian_7():
    p = Permutation(1, 2, 3, 4, 5, 6)
    assert p.is_abelian() == False


def test_is_abelian_8():
    p = Permutation(1, 2, 3, 4, 5, 6, 7)
    assert p.is_abelian() == False


@pytest.mark.parametrize("permutation_input", [
    generate_random_permutation(100) for _ in range(100)
])
def test_constructor_xx(permutation_input):
    p = Permutation(*permutation_input)
    assert p.is_abelian() == False
