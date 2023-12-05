import pytest
from permutation import Permutation

def test_constructor_1():
    p = Permutation()
    assert p.permutation == []

def test_consructor_2():
    p = Permutation(1)
    assert p.permutation == [1]

def test_constructor_3():
    p = Permutation(1, 2, 3, 4, 5)
    assert p.permutation == [1, 2, 3, 4, 5]

def test_constructor_4():
    p = Permutation(5, 1, 3, 2, 4)
    assert p.permutation == [5, 1, 3, 2, 4]

def test_constructor_5():
    with pytest.raises(AssertionError, match=r"-1 is not a natural Number"):
        p = Permutation(-1)

def test_constructor_6():
    with pytest.raises(AssertionError, match=r"-3 is not a natural Number"):
        p = Permutation(4, 2, 1, -3)

def test_constructor_7():
    with pytest.raises(AssertionError, match=r"Permutation is not bijektiv"):
        p = Permutation(1, 2, 3, 4, 4)

def test_constructor_8():
    with pytest.raises(AssertionError, match=r"0.5 is not a natural Number"):
        p = Permutation(1, 2, 3, 4, 0.5)

def test_constructor_9():
    with pytest.raises(AssertionError, match=r"2 is not a natural Number between 1 and 1"):
        p = Permutation(2) 

def test_constructor_10():
    with pytest.raises(AssertionError, match=r"10 is not a natural Number between 1 and 5"):
        p = Permutation(1, 2, 3, 4, 10) 
