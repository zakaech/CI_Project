import pytest
from calculator import addition, soustraction, multiplication, division


def test_addition():
    assert addition(2, 3) == 5


def test_soustraction():
    assert soustraction(5, 3) == 2


def test_multiplication():
    assert multiplication(2, 3) == 6


def test_division():
    assert division(6, 2) == 3


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(10, 0)