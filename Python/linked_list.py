"""Linked List"""

class Node(object):
    """Linked list node"""
    def __init__(self, data):
        self.data = data
        self.nextn = None

    def __str__(self):
        outstring = ''
        node = self
        while node:
            outstring += str(node.data)
            node = node.nextn
            if node:
                outstring += ' -- '
        return outstring

    def push_to_tail(self, data):
        """Append a node to the list's tail. The node traverse the entire
        list"""
        node = self
        while node:
            if node.nextn:
                node = node.nextn
            else:
                node.nextn = Node(data)
                break


# if __name__ == '__main__':
#     lst = Node('a')
#     lst.push_to_tail('b')
#     lst.push_to_tail('c')
#     print lst
