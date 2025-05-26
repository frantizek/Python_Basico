import pytest
import math
from math_functions import (
    get_absolute_value, get_remainder, get_power, get_ceiling,
    get_floor, get_fractional_and_integer_parts, get_factorial
)

def test_absolute_value():
    assert get_absolute_value(-5) == 5.0
    assert get_absolute_value(5) == 5.0
    assert get_absolute_value(0) == 0.0

def test_remainder():
    assert get_remainder(5, 2) == 1.0
    assert get_remainder(10, 3) == 1.0
    assert get_remainder(-5, 2) == -1.0

def test_power():
    assert get_power(5, 3) == 125.0
    assert get_power(2, 10) == 1024.0
    assert get_power(10, 0) == 1.0

def test_ceiling():
    assert get_ceiling(5.2) == 6
    assert get_ceiling(5.0) == 5
    assert get_ceiling(-5.2) == -5

def test_floor():
    assert get_floor(5.2) == 5
    assert get_floor(5.0) == 5
    assert get_floor(-5.2) == -6

def test_fractional_and_integer_parts():
    assert get_fractional_and_integer_parts(50.5) == (0.5, 50.0)
    fractional, integer = get_fractional_and_integer_parts(10.75)
    assert pytest.approx(fractional) == 0.75
    assert integer == 10.0

def test_factorial():
    assert get_factorial(5) == 120
    assert get_factorial(0) == 1
    assert get_factorial(1) == 1
    
    # Test for error cases
    with pytest.raises(ValueError):
        get_factorial(-1)