"""."""
from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """This is a queue."""

    def __init__(self, iterable=None):
        """."""
        self.dll = DoublyLinkedList()

    def enqueue(self, val):
        """."""
        self.dll.push(val)

    def dequeue(self):
        """."""
        return self.dll.shift()

    def clear(self):
        """."""
        pass

    def __len__(self):
        """."""
        return self.dll.__len__()