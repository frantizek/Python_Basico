import pytest
import math
from math_functions import (
    get_absolute_value, get_remainder, get_power, get_ceiling,
    get_floor, get_fractional_and_integer_parts, get_factorial
)

@pytest.mark.parametrize("input_value, expected", [
    (-5, 5.0),
    (5, 5.0),
    (0, 0.0)
])
def test_absolute_value(input_value, expected):
    assert get_absolute_value(input_value) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 2, 1.0),
    (10, 3, 1.0),
    (-5, 2, -1.0)
])
def test_remainder(x, y, expected):
    assert get_remainder(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 125.0),
    (2, 10, 1024.0),
    (10, 0, 1.0)
])
def test_power(x, y, expected):
    assert get_power(x, y) == expected

@pytest.mark.parametrize("input_value, expected", [
    (5.2, 6),
    (5.0, 5),
    (-5.2, -5)
])
def test_ceiling(input_value, expected):
    assert get_ceiling(input_value) == expected

@pytest.mark.parametrize("input_value, expected", [
    (5.2, 5),
    (5.0, 5),
    (-5.2, -6)
])
def test_floor(input_value, expected):
    assert get_floor(input_value) == expected

@pytest.mark.parametrize("input_value, expected_fractional, expected_integer", [
    (50.5, 0.5, 50.0),
    (10.75, 0.75, 10.0),
    (-3.25, -0.25, -3.0)
])
def test_fractional_and_integer_parts(input_value, expected_fractional, expected_integer):
    fractional, integer = get_fractional_and_integer_parts(input_value)
    assert pytest.approx(fractional) == expected_fractional
    assert integer == expected_integer

@pytest.mark.parametrize("input_value, expected", [
    (5, 120),
    (0, 1),
    (1, 1)
])
def test_factorial(input_value, expected):
    assert get_factorial(input_value) == expected

def test_factorial_raises_error():
    with pytest.raises(ValueError):
        get_factorial(-1)