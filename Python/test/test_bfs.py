"""Tests for the BFS module"""

import unittest
from bfs import bfsTraverse


class test_bfsTraverse(unittest.TestCase):
    """Test the correct order in traversing a graph"""
    def setUp(self):
        """Create a graph and a tuple with the correct traverse"""
        self.correctResTup = ('a', 'b', 'd', 'g', 'e', 'f', 'c', 'h')
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
        result = bfsTraverse(self.graphDict, 'a')
        self.assertEqual(result, self.correctResTup)


if __name__ == '__main__':
    unittest.main()
