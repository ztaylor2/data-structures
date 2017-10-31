"""A max heap in python."""


class Heap(object):
    """A max heap."""

    def __init__(self):
        """Init the heap."""
        self.heap_list = []

    def _parent_index_of_left_child(self, left_child_index):
        """Find the index of the parent node from the index of the left child node."""
        return ((left_child_index - 1) / 2)

    def _parent_index_of_right_child(self, right_child_index):
        """Find the parent index from the index of the right child node."""
        return ((right_child_index - 2) / 2)

    def _left_child_index_from_parent(self, parent_index):
        """Find the left child index from the index of the parent node."""
        return parent_index * 2 + 1

    def _right_child_index_from_parent(self, parent_index):
        """Find the right child index from the index of the parent node."""
        return parent_index * 2 + 2

    def _parent_value_of_child(self, child_index):
        """."""
        if child_index % 2 == 0:
            parent_index = self._parent_index_of_right_child(self, child_index)
        else:
            parent_index = self._parent_index_of_left_child(self, child_index)
        return self.heap_list[parent_index]

    def push(self, val):
        """."""
        self.heap_list.append(val)
        # call sort function when it is built
