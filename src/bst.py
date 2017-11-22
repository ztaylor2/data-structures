"""A binary search tree written in python."""


class Node(object):
    """The node class."""

    def __init__(self, val, right=None, left=None, parent=None, depth=1):
        """On initialization."""
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent


class BinarySearchTree(object):
    """Binary Search Tree."""

    def __init__(self, val=None):
        """Init top node."""
        self.root = Node(val)
        self.size_count = 0
        if val:
            self.size_count += 1
        self.depths_list = []
        self.left_depths_list = []
        self.right_depths_list = []

    def insert(self, val):
        """Insert node."""
        if self.root.val:
            current = self.root
            while current:
                if val > current.val:
                    if not current.right:
                        current.right = Node(val, None, None, current)
                        self.size_count += 1
                        return
                    current = current.right
                elif val < current.val:
                    if not current.left:
                        current.left = Node(val, None, None, current)
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
        self.depths_list = []
        depth = 0
        if self.root.val:
            self._depth_fxn(self.root, depth + 1)
            return max(self.depths_list)
        return depth

    def _depth_fxn(self, current, depth):
        if current.right is None and current.left is None:
            self.depths_list.append(depth)
            return
        if current.right:
            return self._depth_fxn(current.right, depth + 1)
        if current.left:
            return self._depth_fxn(current.left, depth + 1)

    def contains(self, val):
        """Check existance, return boolean."""
        if self.search(val):
            return True
        return False

    def balance(self):
        """Return tree balance."""
        self.depths_list = []
        left_depth = 0
        if self.root.left:
            self._depth_fxn(self.root.left, left_depth + 1)
            left_depth = max(self.depths_list)

        self.depths_list = []
        right_depth = 0
        if self.root.right:
            self._depth_fxn(self.root.right, right_depth + 1)
            right_depth = max(self.depths_list)

        return left_depth - right_depth
