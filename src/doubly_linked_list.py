"""Doubly linked list in python."""

from linked_list import LinkedList


class Node(object):
    """A node for a doubly linked list."""

    def __init__(self, data, next, prev):
        """Build node attributes."""
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    """A doubly linked list."""

    def __init__(self):
        """Initialize dbl linked list."""
        self.list = LinkedList()
        self.list.head

    def push(self, val):
        """Insert value at the beginning of the list."""
        self.list.push(val)

    def append(self, val):
        """Append value to end of list."""

    def pop(self):
        """Pop a value of the beginning of the list."""

    def shift(self):
        """Remove the value from the tail of the list."""

    def remove(self, val):
        """Remove specified value from list."""