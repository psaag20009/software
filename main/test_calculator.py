import pytest

from calculator import Calculator

def test_add():
    calc = Calculator()
    calc.add(5)
    assert calc.amount == 5


def test_add_accumulates():
    calc = Calculator(10)
    calc.add(3)
    assert calc.amount == 13