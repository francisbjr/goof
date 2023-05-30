import calculator
import pytest

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(2,2) == 4
    assert calculator.add(10,5) == 15

def test_subtract():
    assert calculator.subtract(5,2) == 3
    assert calculator.subtract(0,1) == -1

def test_multiply():
    assert calculator.multiply(2,3) == 6
    assert calculator.multiply(5,2) == 10

def test_divide():
    assert calculator.divide(6,3) == 2
    assert calculator.divide(14,2) == 7

def test_exponent():
    assert calculator.exponent(10,2) == 100
    assert calculator.exponent(3,3) == 27