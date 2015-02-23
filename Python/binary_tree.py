"""
Binary Tree module
"""

class BinaryNode(object):
    """
    Representation of a node in a binary tree.
    """
    def __init__(self, key):
        """Create a new leaf labeled with key."""
        self.key = key
        self._left = None
        self._right = None
        self._parent = None

    def overwrite(self, node):
        self.key = node.key
        self.left = node.left
        self.right = node.right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, node):
        if self._left:
            self._left._parent = None
        self._left = node
        if node:
            node._parent = self

    @right.setter
    def right(self, node):
        if self._right:
            self._right._parent = None
        self._right = node
        if node:
            node._parent = self

    @property
    def parent(self):
        return self._parent


class BinaryTree(object):
    """
    Simple binary tree implementation.
    """

    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root:
            return False
        else:
            return True

    def insert(self, key):
        """Insert node labeled key into the tree."""
        new = BinaryNode(key)
        if self.is_empty():
            self.root = new
        else:
            node = self.root
            while True:
                if key < node.key:
                    # Go left
                    if not node.left:
                        node.left = new
                        break
                    node = node.left
                else:
                    # Go right
                    if not node.right:
                        node.right = new
                        break
                    node = node.right
        return new

    def has(self, key):
        """Return True if the tree contains a node labeled key, False
        otherwise."""
        if self._find(key):
            return True
        else:
            return False

    def find_min(self):
        return self.find_min_node().key

    def find_max(self):
        return self.find_max_node().key

    def find_min_node(self, node=None):
        """Return the minimum node. If node is provided, return the minimum
        node in such subtree.
        """
        if not node:
            node = self.root
        while True:
            if node.left:
                node = node.left
            else:
                return node

    def find_max_node(self, node=None):
        """Return the maximum node. If node is provided, return the maximum
        node in such subtree.
        """
        if not node:
            node = self.root
        while True:
            if node.right:
                node = node.right
            else:
                return node

    def delete(self, key):
        """Delete a node labeled key in the tree"""
        node = self._find(key)
        if not node:
            raise KeyError('Key {} not in the tree'.format(key))
        else:
            self.remove(node)

    def remove(self, node):
        """Remove a given node from the tree."""
        while node:
            if not node.left and not node.right:
                if node.parent:
                    if node is node.parent.left:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                    node = None
                else:
                    self.root = None
                    node = None
            elif node.left and not node.right:
                node.overwrite(node.left)
                node = None
            elif not node.left and node.right:
                node.overwrite(node.right)
                node = None
            else:
                subst = self.find_min_node(node.right)
                node.key = subst.key
                node = subst

    def inorder_gen(self, node=None):
        """Generate the in order visit of the tree"""
        node = self.root
        if node:
            node = node
        node_stack = []

        while node_stack or node is not None:
            if node is not None:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop()
                key = node.key
                node = node.right
                yield key

    def _find(self, key):
        """Return the node labeled key, None otherwise."""
        node = self.root
        while node:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

