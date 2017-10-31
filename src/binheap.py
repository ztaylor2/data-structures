"""A max heap in python."""


class Heap(object):
    """A max heap."""

    def __init__(self):
        self.heap_list = []

    def parent_index_of_left_child(self, left_child_index):
        """Find the index of the parent node from the index of the left child node."""
        return ((left_child_index - 1) / 2)

    def parent_index_of_right_child(self, right_child_index):
        """Find the parent index from the index of the right child node."""
        return ((right_child_index - 2) / 2)

    def left_child_index_from_parent(self, parent_index):
        """Find the left child index from the index of the parent node."""
        return parent_index * 2 + 1

    def right_child_index_from_parent(self, parent_index):
        """Find the right child index from the index of the parent node."""
        return parent_index * 2 + 2
