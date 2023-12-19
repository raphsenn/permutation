import pytest
from permutation.permutation import Permutation
from extra.random_permutation import generate_random_permutation


def test_iverse_1():
    p = Permutation(1)
    assert p.inverse().permutation ==  {1 : 1}


def test_inverse_2():
    p = Permutation(1, 2)
    assert p.inverse().permutation == {1 : 1, 2 : 2}


def test_inverse_3():
    p = Permutation(1, 3, 2)
    assert p.inverse().permutation == {1 : 1, 2 : 3, 3 : 2}


def test_inverse_4():
    p = Permutation(3, 2, 1)
    assert (p.inverse()*p).permutation == {1: 1, 2 : 2, 3 : 3}


def test_inverse_5():
    p = Permutation(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert (p*p.inverse()).permutation == {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10}
    assert (p.inverse()*p).permutation == {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10}


# id_100 is like Permutation(1, 2, 3, 4, ..., 100)
id_100 = {i : i for i in range(1, 101)}

@pytest.mark.parametrize("permutation_input", [
    generate_random_permutation(100) for _ in range(100)
])
def test_inverse_100(permutation_input):
    p = Permutation(*permutation_input)
    assert (p.inverse()*p).permutation == id_100
