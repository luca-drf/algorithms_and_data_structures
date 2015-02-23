"""Tests for sorting algorithms"""

import unittest
import random as rnd
from bucket_sort import bucketSort
from counting_sort import countingSort
from merge_sort import MergeSort
from quick_sort import ItrQuickSort, RecQuickSort
from radix_sort import radixSort


class test_SortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.intarray = [rnd.randint(0, 100) for _ in xrange(100)]
        self.floatarray = [rnd.uniform(0, 100) for _ in xrange(100)]
        self.zeroonearray = [rnd.random() for _ in xrange(100)]

    def test_bucketSort(self):
        self.assertEqual(sorted(self.zeroonearray), bucketSort(self.zeroonearray))

    def test_countingSort(self):
        self.assertEqual(sorted(self.intarray), countingSort(self.intarray, 101))

    def test_MergeSort(self):
        self.assertEqual(sorted(self.floatarray), MergeSort(self.floatarray))

    def test_QuickSort(self):
        self.assertEqual(sorted(self.floatarray), ItrQuickSort(self.floatarray,
                                                               0, 99))
        self.assertEqual(sorted(self.floatarray), RecQuickSort(self.floatarray,
                                                               0, 99))
    def test_radixSort(self):
        self.assertEqual(sorted(self.intarray), radixSort(self.intarray, 10))

if __name__ == '__main__':
    unittest.main()

