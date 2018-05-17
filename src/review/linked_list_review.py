"""A linked list in python."""


class Node(object):
    """A node for a linked list."""

    def __init__(self, val, next):
        """Initialize the node."""
        self.val = val
        self.next = next


class LinkedList(object):
    """A linked list data structure."""

    def __init__(self):
        """Initialize the linked list."""
        self.head = None

    def push(self, val):
        """Add a node to the linked list."""
        self.head = Node(val, self.head)

    def pop(self):
        """Pop a value off of the end of the list."""
        if not self.head:
            raise IndexError('Cannot pop from empty linked list.')

        popped_value = self.head.val
        self.head = self.head.next
        return popped_value

    def search(self, val):
        """Search through the linked list."""
        if not self.head:
            raise IndexError('Cannot search empty list.')

        current_node = self.head

        while current_node:
            if current_node.val == val:
                return current_node
            current_node = current_node.next

    def remove(self, val):
        """Remove a value from the linked list."""
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.val == val:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next
