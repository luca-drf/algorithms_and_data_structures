"""Depth First Search on a graph"""

from sets import Set
from linked_list import Node


class lightStack(object):
    """Simple stack"""
    def __init__(self):
        self.head = None

    def push(self, lst):
        """Push a list of nodes"""
        for obj in lst:
            new = Node(obj)
            new.nextn = self.head
            self.head = new

    def pop(self):
        """Returns the top of the stack and then removes it"""
        if self.head:
            popped = self.head
            self.head = popped.nextn
            return popped.data
        else:
            raise IndexError('Popping from empty stack')

    def top(self):
        """Returns the top of the stack"""
        if self.head:
            return self.head.data
        else:
            raise IndexError('Stack is empty')

    def isEmpty(self):
        """Returns True if the the stack is empty, False otherwise"""
        if self.head:
            return False
        else:
            return True


def dfsTraverse(graphDict, start):
    """Returns a tuple with the nodes traversed in DFS order"""
    stack = lightStack()
    notVisited = Set(graphDict.keys())

    stack.push([start])
    notVisited.remove(start)
    result = [start]
    while not stack.isEmpty():
        curNode = stack.top()
        neighbours = graphDict[curNode]
        nextNode = 'z'
        for node in neighbours:
            if node < nextNode and node in notVisited:
                nextNode = node
        if nextNode != 'z':
            stack.push(nextNode)
            result.append(nextNode)
            notVisited.remove(nextNode)
        else:
            stack.pop()

    return tuple(result)
