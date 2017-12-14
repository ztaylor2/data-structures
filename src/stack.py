"""A stack in python."""

from linked_list import LinkedList


class Stack(object):
    """A stack data structure."""

    def __init__(self, iterable=None):
        """Init Stack."""
        self.list = LinkedList()
        self.list.head = None
        self._counter = 0
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.push(item)

    def __len__(self):
        """Return the size of the stack."""
        return self._counter

    def push(self, value):
        """Add a value to the top of stack."""
        if isinstance(value, (tuple, list)):
            for value in value:
                self.list.push(value)
                self._counter += 1
        else:
            self.list.push(value)
            self._counter += 1

    def pop(self):
        """Remove value from top of stack and return it."""
        val = self.list.pop()
        self._counter -= 1
        return val

    def peek(self):
        """Return the next value to be popped."""
        try:
            return self.list.head.data
        except AttributeError:
            return None