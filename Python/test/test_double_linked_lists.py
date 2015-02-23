"""Unit test for binary_tree.py"""
import unittest
import double_linked_lists as dlists


class TestInserAndDeleteFunc(unittest.TestCase):
    """Test insert and delete functions"""
    def setUp(self):
        self.testDLL = dlists.DLL()

    def test_insert_front_order(self):
        """Test if the order of insert_front is preserved in the list"""
        self.testDLL.insert_front(3)
        self.testDLL.insert_front(2)
        self.testDLL.insert_front(1)
        node = self.testDLL.head
        lst = []
        while node:
            lst.append(node.value)
            node = node.right
        self.assertEqual(lst, [1, 2, 3])

    def test_insert_back_order(self):
        """Test if the order of insert_back is preserved in the list"""
        self.testDLL.insert_back(3)
        self.testDLL.insert_back(2)
        self.testDLL.insert_back(1)
        node = self.testDLL.head
        lst = []
        while node:
            lst.append(node.value)
            node = node.right
        self.assertEqual(lst, [3, 2, 1])

    def test_extract_element(self):
        """Test the delete function"""
        self.testDLL.insert_back(3)
        self.testDLL.insert_back(2)
        self.testDLL.insert_back(1)
        res = self.testDLL.extract(2)
        node = self.testDLL.head
        lst = []
        while node:
            lst.append(node.value)
            node = node.right
        self.assertEqual(lst, [3, 1])
        self.assertEqual(res, 2)

    def test_extract_element_on_empty_list(self):
        """Test attempting to extract an element on an empty list"""
        self.assertRaises(KeyError, self.testDLL.extract, 2)


class TestOutput(unittest.TestCase):
    """Test output and conversion functions"""
    def setUp(self):
        self.plist = [1, 2, 3, 4, 5]
        self.testDLL = dlists.DLL()
        for val in self.plist:
            self.testDLL.insert_back(val)

    def test_to_list(self):
        """Test if to_list returns a correct python list"""
        lst = self.testDLL.to_list()
        self.assertEqual(lst, self.plist)

    def test_seek_list(self):
        """Test if the double link works"""
        node = self.testDLL.head
        lstr = []
        lstl = []
        while node:
            lstr.append(node.value)
            node = node.right
        node = self.testDLL.tail
        while node:
            lstl.append(node.value)
            node = node.left
        lstr.reverse()
        self.assertEqual(lstl, lstr)


if __name__ == "__main__":
    unittest.main()
