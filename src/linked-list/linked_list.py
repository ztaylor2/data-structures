"""A linked list in python."""


class Node(object):
    """."""

    def __init__(self):
        """Build node attributes."""
        self.data = None
        self.next = None


class LinkedList(object):
    """Create linked list object."""

    def __init__(self, iterable=None):
        """Head node is none on init."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, data):
        """Push value to linked list."""
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node
        self._counter += 1

    def pop(self):
        """Remove first item from list and return it."""
        if not self.head:
            raise IndexError("List is empty.")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def size(self):
        """."""
        return self._counter

    def search(self, val):
        """."""
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

    def remove(self, node):
        """."""
        pass

    def display(self):
        """."""
        output_sting = "\"("
        node = self.head
        while node:
            try:
                float(node.data)
                output_sting += (str(node.data) + ", ")
            except ValueError:
                output_sting += ("\'" + node.data + "\'") + ", "
            node = node.next
        output_sting = output_sting[:-2] + ')\"'
        print(output_sting)

    def __len__(self):
        """Return size of linked list."""
        return self._counter

    def __str__(self):
        """Return what the display method returns."""
        pass

myList = LinkedList()
