import unittest
from zigzag import (
    solution,
)
class BankAccountTest(unittest.TestCase):
    def test_001(self):
        self.assertEqual(solution([1, 2, 1, 3, 4]), [1, 1, 0])


    def test_002(self):
        self.assertEqual(solution([1, 2, 3, 4]), [0, 0])


    def test_003(self):
        self.assertEqual(solution([1000000000, 1000000000, 1000000000]), [0])


    def test_004(self):
        self.assertEqual(solution([1, 2, 4, 3, 1]), [0, 1, 0])


    def test_005(self):
        self.assertEqual(solution([3, 5, 2, 6, 10]), [1, 1, 0])


    def test_006(self):
        self.assertEqual(solution([1, 3, 4, 5, 6, 14, 14]), [0, 0, 0, 0, 0])


    def test_007(self):
        self.assertEqual(solution([1, 5, 7, 3, 10, 2, 4, 9, 8, 6]), [0, 1, 1, 1, 1, 0, 1, 0])


    def test_008(self):
        self.assertEqual(solution([11, 14, 3, 17, 16, 13, 3, 7, 19, 8]), [1, 1, 1, 0, 0, 1, 0, 1])