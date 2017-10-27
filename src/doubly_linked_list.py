"""Doubly linked list in python."""

from linked_list import LinkedList


class Node(object):
    """A node for a doubly linked list."""

    def __init__(self, data=None, next_node=None, prev=None):
        """Build node attributes."""
        self.data = data
        self.next_node = next_node
        self.prev = prev


class DoublyLinkedList(object):
    """A doubly linked list."""

    def __init__(self, iterable=None):
        """Initialize dbl linked list."""
        self.list = LinkedList()
        self.head = None
        self.tail = None
        self._counter = 0
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.append(item)

    def __len__(self):
        """Return length of list."""
        return self._counter

    def push(self, val):
        """Insert value at the beginning of the list."""
        new_node = Node(val, self.head)
        if len(self) == 0:
            self.tail = new_node
        elif len(self) > 0:
            self.head.prev = new_node
        self.head = new_node
        self._counter += 1

    def append(self, val):
        """Append value to end of list."""
        new_node = Node(val, None, self.tail)
        if len(self) == 0:
            self.head = new_node
        elif len(self) > 0:
            self.tail.next_node = new_node
        self.tail = new_node
        self._counter += 1

    def pop(self):
        """Pop a value off the beginning of the list."""
        try:
            output = self.head.data
            self.head = self.head.next_node
            self._counter -= 1
            return output
        except AttributeError:
            raise IndexError('Cannot pop empty list.')

    def shift(self):
        """Remove the value from the tail of the list."""
        try:
            output = self.tail.data
            self.tail = self.tail.prev
            self._counter -= 1
            return output
        except AttributeError:
            raise IndexError('Cannot shift empty list.')

    def remove(self, val):
        """Remove specified value from list."""
        if self.head is self.tail and val == self.head.data:
            self.head = self.tail = None
            return
        curr_node = self.head
        while curr_node:
            if curr_node.data == val:
                curr_node.prev.next_node = curr_node.next_node
                curr_node.next_node.prev = curr_node.prev
                self._counter -= 1
                return
            curr_node = curr_node.next_node
        raise ValueError('Value not in list.')
