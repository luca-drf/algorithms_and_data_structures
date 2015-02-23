class Node:
    def __init__(self, data):
        self.data = data
        self.nextn = None


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top:
            value = self.top.data
            self.top = self.top.nextn
            return value
        else:
            raise IndexError('The stack is empty')

    def push(self, data):
        newtop = Node(data)
        if self.top:
            newtop.nextn = self.top
        self.top = newtop

    def __str__(self):
        outstr = ''
        node = self.top
        while node:
            outstr += '\n'
            outstr += node.data
            node = node.nextn
        return outstr


# if __name__ == '__main__':
#     pile = Stack()
#     pile.push('a')
#     pile.push('b')
#     pile.push('c')
#     try:
#         print pile.pop()
#         print pile.pop()
#         print pile.pop()
#         print pile.pop()
#     except IndexError:
#         print 'Stack is empty'

#     print pile
