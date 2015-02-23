"""Breadth First Search on a graph"""

from sets import Set
from linked_list import Node


class lightQueue(object):
    """Simple queue"""
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, lst):
        """Enqueue a list of nodes"""
        for obj in lst:
            if self.head:
                self.tail.nextn = Node(obj)
                self.tail = self.tail.nextn
            else:
                self.tail = Node(obj)
                self.head = self.tail

    def dequeue(self):
        """Returns the head of the queue"""
        if self.head:
            popped = self.head
            self.head = popped.nextn
            return popped.data
        else:
            raise IndexError('Popping from empty queue')

    def isEmpty(self):
        """Returns True if the the queue is empty, False otherwise"""
        if self.head:
            return False
        else:
            return True


def bfsTraverse(graphDict, start):
    """Returns a tuple with the nodes traversed in BFS order"""
    queue = lightQueue()
    notVisited = Set(graphDict.keys())

    queue.enqueue([start])
    notVisited.remove(start)
    result = [start]
    while not queue.isEmpty():
        curNode = queue.dequeue()
        neighbours = graphDict[curNode]
        toSort = []
        for node in neighbours:
            if node in notVisited:
                toSort.append(node)
                notVisited.remove(node)
        toSort.sort()
        queue.enqueue(toSort)
        result.extend(toSort)
    return tuple(result)
