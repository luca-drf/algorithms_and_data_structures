"""Tests for the DFS module"""

import unittest
from dfs import dfsTraverse


class test_dfsTraverse(unittest.TestCase):
    """Test the correct order in traversing a graph"""
    def setUp(self):
        """Create a graph and a tuple with the correct traverse"""
        self.correctResTup = ('a', 'b', 'e', 'g', 'f', 'c', 'h', 'd')
        self.graphDict = {'a': ('b', 'g', 'd'),
                          'b': ('e', 'a', 'f'),
                          'd': ('a', 'f'),
                          'e': ('b', 'g'),
                          'g': ('e', 'a'),
                          'f': ('b', 'd', 'c'),
                          'c': ('f', 'h'),
                          'h': ('c')}

    def test_traverse(self):
        """Test the traverse function"""
        result = dfsTraverse(self.graphDict, 'a')
        self.assertEqual(result, self.correctResTup)


if __name__ == '__main__':
    unittest.main()
