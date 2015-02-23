"""Tests for the binary tree module"""

import unittest
from binary_tree import BinaryTree


class test_BinaryTree(unittest.TestCase):
    def setUp(self):
        self.empty_tree = BinaryTree()
        self.tree = BinaryTree()
        self.tree.insert(3)
        self.tree.insert(4)
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(20)
        self.tree.insert(5)

    def test_has(self):
        self.assertTrue(self.tree.has(3))
        self.assertTrue(self.tree.has(4))
        self.assertTrue(self.tree.has(2))
        self.assertTrue(self.tree.has(1))
        self.assertTrue(self.tree.has(20))
        self.assertTrue(self.tree.has(5))
        self.assertFalse(self.tree.has(11))

    def test_find_min(self):
        self.assertEqual(1, self.tree.find_min())

    def test_find_max(self):
        self.assertEqual(20, self.tree.find_max())

    def test_delete(self):
        self.assertTrue(self.tree.has(3))
        self.tree.delete(3)
        self.assertFalse(self.tree.has(3))
        self.tree.delete(4)
        self.tree.delete(2)
        self.tree.delete(1)
        self.tree.delete(20)
        self.tree.delete(5) 
        self.assertTrue(self.tree.is_empty())

    def test_inorder_gen(self):
        visit = [_ for _ in self.tree.inorder_gen()]
        correct_visit = [1, 2, 3, 4, 5, 20]
        self.assertEqual(correct_visit, visit)


if __name__ == '__main__':
    unittest.main()
