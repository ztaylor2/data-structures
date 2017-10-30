"""This is a deque data structure."""

from doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Deque data structure, can add and remove from both ends."""

    def __init__(self):
        """Initialize the deque."""
        self.deque = DoublyLinkedList()

    def append(self, value):
        """Add an item to the back of the deque."""
        self.deque.append(value)

    def appendleft(self, value):
        """Add an item to the front of the deque."""
        self.deque.push(value)

    def pop(self):
        """Pop a value off of the back of the deque and return it."""
        return self.deque.shift()

    def popleft(self):
        """Pop a value off of the front of the deque and return it."""
        return self.deque.pop()
