"""This is a deque data structure."""

from doubly_linked_list import DoublyLinkedList


class deque(object):
    """Deque data structure, can add and remove from both ends."""

    def __init__(self):
        self.deque = DoublyLinkedList()

    def append(self, value):
        self.deque.append(value)

    def appendleft(self, value):
        self.deque.push(value)