import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98
    
def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(-10, 2) == -5
    assert calculator.divide(-10, -2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


def test_divide_invalid_input():
    with pytest.raises(ValueError):
        calculator.divide("10", 2
)
def test_divide_zero_numerator():
    assert calculator.divide(0, 5) == 0

def test_divide_floats():
    assert calculator.divide(7.5, 2.5) == 3

def test_divide_small_numbers():
    assert calculator.divide(1, 4) == 0.25

def test_divide_invalid_denominator():
    with pytest.raises(ValueError):
        calculator.divide(10, "2")

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(2, -1) == 0.5


def test_power_invalid_input():
    with pytest.raises(ValueError):
        calculator.power("2", 3)


def test_average():
    assert calculator.average(10, 20) == 15
    assert calculator.average(-10, 10) == 0
    assert calculator.average(2.5, 3.5) == 3


def test_average_invalid_input():
    with pytest.raises(ValueError):
        calculator.average(10, "20")


def test_percentage():
    assert calculator.percentage(25, 100) == 25
    assert calculator.percentage(1, 4) == 25
    assert calculator.percentage(50, 200) == 25


def test_percentage_zero_total():
    with pytest.raises(ZeroDivisionError):
        calculator.percentage(10, 0)


def test_percentage_invalid_input():
    with pytest.raises(ValueError):
        calculator.percentage("25", 100)
