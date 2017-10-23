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
        output_sting = "\"("
        node = self.head
        while node:
            output_sting += (str(node.data) + ", ")
            node = node.next
        output_sting = output_sting[:-2]
        output_sting += ')\"'
        print(output_sting)

# output should look like:
#         “(12, ‘sam’, 37, ‘tango’)”

    def __len__(self):
        """Return size of linked list."""
        pass

    def __str__(self):
        """Return what the display method returns."""
        pass

myList = LinkedList()
