"""A linked list in python."""


class Node(object):
    """."""

    def __init__(self):
        """."""
        self.data = None
        self.next = None


class LinkedList(object):
    """."""

    def __init__(self):
        """."""
        self.head = None

    def push(self, data):
        """Push value to linked list."""
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """."""
        pass

    def size(self):
        """."""
        pass

    def search(self, val):
        """."""
        pass

    def remove(self, node):
        """."""
        pass

    def display(self):
        """."""
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def __len__(self):
        """Return size of linked list."""
        pass

    def __str__(self):
        """Return what the display method returns."""
        pass

myList = LinkedList()
