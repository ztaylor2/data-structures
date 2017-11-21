"""A binary search tree written in python."""


class Node(object):
    """The node class."""

    def __init__(self, val, right=None, left=None):
        """On initialization."""
        self.val = val
        self.right = right
        self.left = left


class BinarySearchTree(object):
    """Binary Search Tree."""

    def __init__(self, val=None):
        """Init top node."""
        self.root = Node(val)
        self.size_count = 0
        if val:
            self.size_count += 1

    def insert(self, val):
        """Insert node."""
        if self.root.val:
            current = self.root
            while current:
                if val > current.val:
                    if not current.right:
                        current.right = Node(val)
                        self.size_count += 1
                        return
                    current = current.right
                elif val < current.val:
                    if not current.left:
                        current.left = Node(val)
                        self.size_count += 1
                        return
                    current = current.left
        self.root.val = val

    def search(self, val):
        """Return node containing val."""
        current = self.root
        return self._search(current, val)

    def _search(self, current, val):
        """Recursive search function."""
        if current.val == val:
            return current
        if current.val < val:
            if current.right:
                return self._search(current.right, val)
        if current.val > val:
            if current.left:
                return self._search(current.left, val)

    def size(self):
        """Return size."""
        return self.size_count

    def depth(self):
        """Return depth."""



    def contains(self, val):
        """Check existance, return boolean."""

    def balance(self):
        """Return tree balance."""
