"""A linked list in python."""


class Node(object):
    """."""

    def __init__(self, data, next):
        """Build node attributes."""
        self.data = data
        self.next = next


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
        new_node = Node(data, self.head)
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

    def display(self):
        """."""
        output_string = "("
        node = self.head
        if node is None:
            return '()'
        while node:
            try:
                float(node.data)
                output_string += (str(node.data) + ", ")
            except ValueError:
                output_string += ("\'" + node.data + "\'") + ", "
            node = node.next
        output_string = output_string[:-2] + ')'
        return(output_string)

    def __len__(self):
        """Return size of linked list."""
        return self._counter

    def remove(self, node):
        """."""
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == node:
                if previous_node is None:
                    self.head = current_node.next
                    self._counter -= 1
                    return
                else:
                    previous_node.next = current_node.next
                    self._counter -= 1
                    return
            else:
                previous_node = current_node
                current_node = current_node.next
        raise IndexError('Node not in linked list.')

    def __str__(self):
        """Return what the display method returns."""
        return self.display()

