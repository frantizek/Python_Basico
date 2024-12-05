import unittest
from steps_to_kaprekars_constant import steps_to_kaprekars_constant

class MyTestCase(unittest.TestCase):
    def test_basic_behaviour(self):
        self.assertEqual(steps_to_kaprekars_constant(0), 0)  # add assertion here
        self.assertEqual(steps_to_kaprekars_constant(6174), 1)
        self.assertEqual(steps_to_kaprekars_constant(9904), 7)
        self.assertEqual(steps_to_kaprekars_constant(3333), 0)
        self.assertEqual(steps_to_kaprekars_constant(4017), 6)


    def test_all_digits_equal(self):
        self.assertEqual(steps_to_kaprekars_constant(0), 0)
        self.assertEqual(steps_to_kaprekars_constant(1111), 0)
        self.assertNotEqual(steps_to_kaprekars_constant(2222), 3)
        self.assertEqual(steps_to_kaprekars_constant(3333), 0)

    def test_out_of_range_numbers(self):
        self.assertEqual(steps_to_kaprekars_constant(-1), -1)
        self.assertEqual(steps_to_kaprekars_constant(11111), -1)

if __name__ == '__main__':
    unittest.main()
