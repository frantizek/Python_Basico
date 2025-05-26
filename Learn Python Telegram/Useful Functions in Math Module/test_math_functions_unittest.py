import unittest
import math
from math_functions import (
    get_absolute_value, get_remainder, get_power, get_ceiling,
    get_floor, get_fractional_and_integer_parts, get_factorial
)

class TestMathFunctions(unittest.TestCase):
    
    def test_absolute_value(self):
        self.assertEqual(get_absolute_value(-5), 5.0)
        self.assertEqual(get_absolute_value(5), 5.0)
        self.assertEqual(get_absolute_value(0), 0.0)
    
    def test_remainder(self):
        self.assertEqual(get_remainder(5, 2), 1.0)
        self.assertEqual(get_remainder(10, 3), 1.0)
        self.assertEqual(get_remainder(-5, 2), -1.0)
    
    def test_power(self):
        self.assertEqual(get_power(5, 3), 125.0)
        self.assertEqual(get_power(2, 10), 1024.0)
        self.assertEqual(get_power(10, 0), 1.0)
    
    def test_ceiling(self):
        self.assertEqual(get_ceiling(5.2), 6)
        self.assertEqual(get_ceiling(5.0), 5)
        self.assertEqual(get_ceiling(-5.2), -5)
    
    def test_floor(self):
        self.assertEqual(get_floor(5.2), 5)
        self.assertEqual(get_floor(5.0), 5)
        self.assertEqual(get_floor(-5.2), -6)
    
    def test_fractional_and_integer_parts(self):
        self.assertEqual(get_fractional_and_integer_parts(50.5), (0.5, 50.0))
        fractional, integer = get_fractional_and_integer_parts(10.75)
        self.assertAlmostEqual(fractional, 0.75)
        self.assertEqual(integer, 10.0)
    
    def test_factorial(self):
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(0), 1)
        self.assertEqual(get_factorial(1), 1)
        
        # Test for error cases
        with self.assertRaises(ValueError):
            get_factorial(-1)

if __name__ == '__main__':
    unittest.main()