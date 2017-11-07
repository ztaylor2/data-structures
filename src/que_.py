"""."""
from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """This is a queue."""

    def __init__(self, iterable=None):
        """Initialize Queue object."""
        self.dll = DoublyLinkedList()

    def enqueue(self, val):
        """Add val to head of queue."""
        if isinstance(val, (tuple, list)):
            for val in val:
                self.enqueue(val)
        else:
            self.dll.push(val)

    def dequeue(self):
        """Remove val from tail of queue."""
        try:
            return self.dll.shift()
        except IndexError:
            raise IndexError('Cannot shift empty queue.')

    def peek(self):
        """Look at next val to be dequeued without mod queue."""
        try:
            return self.dll.tail.data
        except AttributeError:
            return None

    def __len__(self):
        """Return length of queue."""
        return self.dll.__len__()
