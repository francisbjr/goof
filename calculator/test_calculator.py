import calculator
import pytest

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(2,2) == 4
    assert calculator.add(10,5) == 15

def test_subtraction():
    assert calculator.subtraction(5,2) == 3