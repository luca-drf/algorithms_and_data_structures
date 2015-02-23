"""Tests for the Binary Search module"""

import unittest
from binary_search import RecBinarySearch, ItrBinarySearch


class test_BinarySearch(unittest.TestCase):
    """ Test correctness of all binary search implementations"""
    def setUp(self):
        self.array = (1, 2, 3, 4, 5, 6, 7)

    def test_RecBinarySearch_fail(self):
        self.assertEqual(-1, RecBinarySearch(self.array, 0, 0, 6))
        self.assertEqual(-1, RecBinarySearch(self.array, 8, 0, 6))

    def test_RecBinarySearch_succes(self):
        self.assertEqual(5, RecBinarySearch(self.array, 6, 0, 6))
        self.assertEqual(1, RecBinarySearch(self.array, 2, 0, 6))

    def test_ItrBinarySearch_fail(self):
        self.assertEqual(-1, ItrBinarySearch(self.array, 0, 0, 6))
        self.assertEqual(-1, ItrBinarySearch(self.array, 8, 0, 6))

    def test_ItrBinarySearch_succes(self):
        self.assertEqual(5, ItrBinarySearch(self.array, 6, 0, 6))
        self.assertEqual(1, ItrBinarySearch(self.array, 2, 0, 6))


if __name__ == '__main__':
    unittest.main()
