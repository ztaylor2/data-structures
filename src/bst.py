"""A binary search tree written in python."""

import timeit
from que_ import Queue


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
        self.size_count = 0
        if isinstance(val, (list, tuple)):
            self.root = Node(val[0])
            self.size_count += 1
            for num in val[1:]:
                self.insert(num)
        else:
            self.root = Node(val)
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

    def balance(self, node=None):
        """Return tree balance."""
        if not node:
            node = self.root
        self.depths_list = []
        left_depth = 0
        if node.left:
            self._depth_fxn(node.left, left_depth + 1)
            left_depth = max(self.depths_list)

        self.depths_list = []
        right_depth = 0
        if node.right:
            self._depth_fxn(node.right, right_depth + 1)
            right_depth = max(self.depths_list)

        return left_depth - right_depth

    def in_order(self, recurse=None):
        """Call iterable traversal or recursive traversal based on input."""
        if recurse == 'recurse':
            return self._in_order_recurse()
        return self._in_order_iterate()

    def _in_order_recurse(self):
        """In order traversal of binary search tree."""
        if self.size_count == 0:
            raise IndexError("Cannot traverse empty tree.")

        def recurse_tree_in_order(root_node):
            """Recurse tree."""
            if root_node.left:
                yield from recurse_tree_in_order(root_node.left)
            yield root_node.val
            if root_node.right:
                yield from recurse_tree_in_order(root_node.right)
        yield from recurse_tree_in_order(self.root)

    def _in_order_iterate(self):
        """In order traversal solved iteratively."""
        if self.size_count == 0:
            return IndexError("Cannot traverse empty tree.")

        current = self.root
        visited = []

        while len(visited) <= self.size_count:
            if current.left and current.left.val not in visited:
                current = current.left
                continue

            if current.val not in visited:
                visited.append(current.val)
                yield current.val

            if current.right and current.right.val not in visited:
                current = current.right
                continue

            current = current.parent

    def pre_order(self, recurse=None):
        """Pre order traversal."""
        if recurse == 'recurse':
            return self._pre_order_recurse()
        return self._pre_order_iterate()

    def _pre_order_recurse(self):
        """Return a generator that will return values in tree in pre order."""
        if self.size_count == 0:
            raise IndexError("Cannot traverse empty tree.")

        def recurse_tree_pre_order(root_node):
            """Recurse tree in pre order."""
            yield root_node.val
            if root_node.left:
                yield from recurse_tree_pre_order(root_node.left)
            if root_node.right:
                yield from recurse_tree_pre_order(root_node.right)
        yield from recurse_tree_pre_order(self.root)

    def _pre_order_iterate(self):
        """Pre order iteration generator."""
        if self.size_count == 0:
            raise IndexError("Cannot traverse empty tree.")

        visited = []
        current = self.root

        while len(visited) <= self.size_count:
            if current.val not in visited:
                visited.append(current.val)
                yield current.val

            if current.left and current.left.val not in visited:
                current = current.left
                continue

            if current.right and current.right.val not in visited:
                current = current.right
                continue

            current = current.parent

    def post_order(self, recurse=None):
        """Post order traversal."""
        if recurse == 'recurse':
            return self._post_order_recurse()
        return self._post_order_iterate()

    def _post_order_recurse(self):
        """Return generator that returns values in treepost order traversal."""
        if self.size_count == 0:
            raise IndexError("Cannot traverse empty tree.")

        def recurse_tree_post_order(root_node):
            """Recurse tree in pre order."""
            if root_node.left:
                yield from recurse_tree_post_order(root_node.left)
            if root_node.right:
                yield from recurse_tree_post_order(root_node.right)
            yield root_node.val
        yield from recurse_tree_post_order(self.root)

    def _post_order_iterate(self):
        """Iterate for post order traversal."""
        if self.size_count == 0:
            return IndexError("Cannot traverse empty tree.")

        visited = []
        current = self.root

        while len(visited) <= self.size_count:
            if current.left and current.left.val not in visited:
                current = current.left
                continue

            if current.right and current.right.val not in visited:
                current = current.right
                continue

            if current.val not in visited:
                visited.append(current.val)
                yield current.val

            current = current.parent

    def breadth_first(self):
        """Return a generator that returns values tree breadth first order."""
        if self.size_count == 0:
            raise IndexError("Cannot traverse empty tree.")

        breadth_list = Queue()
        breadth_list.enqueue(self.root)
        yield breadth_list.peek().val

        while breadth_list.peek():
            if breadth_list.peek().left:
                breadth_list.enqueue(breadth_list.peek().left)
                yield breadth_list.peek().left.val
            if breadth_list.peek().right:
                breadth_list.enqueue(breadth_list.peek().right)
                yield breadth_list.peek().right.val
            breadth_list.dequeue()

    def delete(self, val):
        """Delete a node."""
        node = self.search(val)

        # leaf node
        if node.left is None and node.right is None:
            if node == node.parent.right:
                node.parent.right = None
            if node == node.parent.left:
                node.parent.left = None
            node.parent = None

        # node to delete has one right child
        if node.right and not node.left:
            if node.parent.right == node:
                node.parent.right = node.right
                node.right.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.right
                node.right.parent = node.parent
            node.parent = None

        # node to delete has one left child
        if node.left and not node.right:
            if node.parent.right == node:
                node.parent.right = node.left
                node.left.parent = node.parent
            if node.parent.left == node:
                node.parent.left = node.left
                node.left.parent = node.parent
            node.parent = None

        if node.right and node.left:
            if self.balance(node) < 0:
                self._delete_right_subrees_leftmost_child(node)

    def _find_right_subtree_leftmost_child(self, node):
        """From given node find right subtrees left most child."""
        current = node.right
        while current.left:
            current = current.left
        return current

    def _find_left_subtree_rightmost_child(self, node):
        """From given node find left subtrees rihgtmost child."""
        current = node.left
        while current.right:
            current = current.right
        return current

    def _delete_right_subrees_leftmost_child(self, node):
        """Delete node with its right subtees leftmost child."""
        swap_node = self._find_right_subtree_leftmost_child(node)
        if swap_node.right:
            swap_node.parent.left = swap_node.right
            swap_node.right.parent = swap_node.parent
        swap_node.parent = node.parent
        swap_node.right = node.right
        swap_node.left = node.left
        node.right.parent = swap_node
        node.left.parent = swap_node
        if node == node.parent.right:
            node.parent.right = swap_node
        if node == node.parent.left:
            node.parent.left = swap_node


def _wrapper(func, *args, **kwargs):
    def _wrapped():
        return func(*args, **kwargs)
    return _wrapped


if __name__ == '__main__':
    worst_case_bst = BinarySearchTree()
    for i in range(15):
        worst_case_bst.insert(i)

    find15 = _wrapper(worst_case_bst.search, 14)
    print(timeit.timeit(find15))

    best_case_bst = BinarySearchTree((100, 50, 200, 25, 75, 150, 250,
                                      12.5, 37.5, 62.5, 87.5, 125, 175,
                                      225, 275))

    find275 = _wrapper(best_case_bst.search, 275)
    print(timeit.timeit(find275))

    # why is this O(n) so much faster?
    list_test = []
    for i in range(15):
        list_test.append(i)

    def bla():
        """."""
        for i in list_test:
            if i == 14:
                return 14

    print(timeit.timeit(bla))
