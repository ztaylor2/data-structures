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
        if len(self) == 0:
            new_node = Node(val, None, None)
            self.head = new_node
            self.tail = new_node
        if len(self) > 0:
            new_node = Node(val, self.head, None)
            self.head.prev = new_node
            self.head = new_node
        self._counter += 1

    def append(self, val):
        """Append value to end of list."""
        if len(self) == 0:
            new_node = Node(val, None, None)
            self.tail = new_node
            self.head = new_node
        if len(self) > 0:
            new_node = Node(val, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node
        self._counter += 1

    def pop(self):
        """Pop a value off the beginning of the list."""
        try:
            output = self.head.data
            self.head = self.head.next
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
        curr_node = self.head
        while curr_node:
            if curr_node.data == val:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            curr_node = curr_node.next
