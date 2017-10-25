"""A stack in python."""

from linked_list import LinkedList


class Stack(LinkedList):
    """A stack data structure."""

    def __init__(self, iterable=None):
        """Init Stack."""
        self.list = LinkedList
        self.list.head = None
        self.list._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.list.push(self, item)

    def __len__(self):
        """Return the size of the stack."""
        return self.list.__len__(self)

    def push(self, value):
        """Add a value to the top of stack."""
        self.list.push(self, value)
        self.list._counter += 1

    def pop(self):
        """Remove value from top of stack and return it."""
        self.list.pop(self)
        self.list._counter -= 1
