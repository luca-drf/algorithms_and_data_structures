"""Double linked list"""

class Node(object):
    """Node of the list"""
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self.value.__str__()

    def __repr__(self):
        return self.value.__repr__()


class DLL(object):
    """Double linked list class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, value):
        """Insert a node in front"""
        if self.head:
            self.head.left = Node(value, None, self.head)
            self.head = self.head.left
        else:
            self.head = Node(value, None, None)
            self.tail = self.head

    def insert_back(self, value):
        """Insert a node on the back"""
        if self.tail:
            self.tail.right = Node(value, self.tail, None)
            self.tail = self.tail.right
        else:
            self.tail = Node(value, None, None)
            self.head = self.tail

    def extract(self, value):
        """Extract a node (value)"""
        res = self.__search(value)
        if res:
            if res.left and res.right:
                res.left.right = res.right
                res.right.left = res.left
            elif res.left and not res.right:
                res.left.right = None
                self.tail = res.left
            elif not res.left and res.right:
                res.right.left = None
                self.head = res.right
            return res.value
        else:
            raise KeyError('Value not found')

    def to_list(self):
        """Converts the double linked list to a python list and returns it"""
        node = self.head
        plist = []
        while node:
            plist.append(node.value)
            node = node.right
        return plist

    def dump(self):
        """Dump the list content on the stdout"""
        node = self.head
        if not node:
            print "Empty"
        while node:
            print node,
            node = node.right
            if node:
                print "--",
        print '\n',

    def __search(self, value):
        """Search a node (value) in the list"""
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.right


# if __name__ == "__main__":
    # lista = DLL()
    # lista.insert_front(2)
    # lista.insert_front(1)
    # lista.insert_back(3)
    # lista.insert_back(4)
    # lista.dump()
    # lista.delete(1)
    # lista.dump()
    # lista.delete(3)
    # lista.dump()
    # lista.delete(2)
    # lista.dump()
