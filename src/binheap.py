"""A max heap in python."""


class Heap(object):
    """A max heap."""

    def __init__(self):
        """Init the heap."""
        self.heap_list = []

    def _parent_index_from_child_index(self, child_index):
        """Find the index of the parent from a child index."""
        if child_index % 2 == 0:
            return ((child_index - 2) // 2)
        return ((child_index - 1) // 2)

    # def _parent_index_of_left_child(self, left_child_index):
    #     """Find the index of the parent node from the index of the left child node."""

    # def _parent_index_of_right_child(self, right_child_index):
    #     """Find the parent index from the index of the right child node."""

    def _left_child_index_from_parent(self, parent_index):
        """Find the left child index from the index of the parent node."""
        return parent_index * 2 + 1

    def _right_child_index_from_parent(self, parent_index):
        """Find the right child index from the index of the parent node."""
        return parent_index * 2 + 2

    def _parent_value_from_child_index(self, child_index):
        """Return the value of the parent from the child indexd."""
        parent_index = self._parent_index_from_child_index(child_index)
        # import pdb; pdb.set_trace()
        return self.heap_list[parent_index]

    def push(self, val):
        """Push a value to the heap and bubble it into place."""
        self.heap_list.append(val)
        self._bubble_up()

    def _bubble_up(self):
        """Bubble up newly inserted element into place."""
        child_index = len(self.heap_list) - 1
        while True:
            parent_index = self._parent_index_from_child_index(child_index)
            parent_value = self._parent_value_from_child_index(child_index)

            if self.heap_list[child_index] > parent_value:
                self._swap(child_index, parent_index)
                child_index = parent_index
            else:
                return

    def _swap_parent_and_child(self, child_index, parent_index):
        """Swap the parent and child values."""
        temp = self.heap_list[parent_index]
        self.heap_list[parent_index] = self.heap_list[child_index]
        self.heap_list[child_index] = temp
