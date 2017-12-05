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
        self.depth = depth
        self.balance_factor = 0


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
        elif val:
            self.root = Node(val)
            self.size_count += 1
        else:
            self.root = None

        self.depths_list = []
        self.left_depths_list = []
        self.right_depths_list = []

    def insert(self, val):
        """Insert node."""
        if self.root:
            current = self.root
            while current:
                if val == current.val:
                    return
                if val > current.val:
                    if not current.right:
                        current.right = Node(val, None, None, current)
                        self._update_depths(current.right)
                        self.size_count += 1
                        return
                    current = current.right
                elif val < current.val:
                    if not current.left:
                        current.left = Node(val, None, None, current)
                        self._update_depths(current.left)
                        self.size_count += 1
                        return
                    current = current.left
        self.root = Node(val)

    def _update_depths(self, node):
        """Update the depths of all parent nodes starting with leif node."""
        current_depth = node.depth
        while node.parent:

            if node.parent.depth < node.depth + 1:
                node.parent.depth = current_depth + 1

            current_depth += 1
            node = node.parent

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
        if not self.root:
            return 0
        return self.root.depth

    def contains(self, val):
        """Check existance, return boolean."""
        if self.search(val):
            return True
        return False

    def balance(self, node=None):
        """Return tree balance."""
        if not node:
            node = self.root

        if not node.right:
            right_depth = 0
        else:
            right_depth = node.right.depth

        if not node.left:
            left_depth = 0
        else:
            left_depth = node.left.depth

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
        if node is None:
            return

        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
                return

            if node == node.parent.right:
                node.parent.right = None

            node.parent.left = None

        if node.right and not node.left:
            if node == self.root:
                self.root = node.right
                self.root.parent = None

            elif node.parent.right == node:
                node.parent.right = node.right
                node.right.parent = node.parent

            elif node.parent.left == node:
                node.parent.left = node.right
                node.right.parent = node.parent

            if node.parent:
                self._rebalance_nodes_up_tree(node)

        if node.left and not node.right:
            if node == self.root:
                self.root = node.left
                self.root.parent = None

            elif node.parent.right == node:
                node.parent.right = node.left
                node.left.parent = node.parent

            elif node.parent.left == node:
                node.parent.left = node.left
                node.left.parent = node.parent

            if node.parent:
                self._rebalance_nodes_up_tree(node)

        if node.right and node.left:
            if self.balance(node) < 0:
                swap_node = self._find_right_subtree_leftmost_child(node)
                swap_node_parent = swap_node.parent
                self._delete_right_subtrees_leftmost_child(node, swap_node)
                self._rebalance_nodes_up_tree(swap_node_parent)

            else:
                swap_node = self._find_left_subtree_rightmost_child(node)
                swap_node_parent = swap_node.parent
                self._delete_left_subtrees_rightmost_child(node, swap_node)
                self._rebalance_nodes_up_tree(swap_node_parent)

        self.size_count -= 1

    def _rebalance_nodes_up_tree(self, node):
        while node:
            self._rebalance_node(node)
            node = node.parent

    def _rebalance_node(self, node):
        """Rebalance a node based on its children."""
        if node.left:
            left_depth = node.left.depth
        else:
            left_depth = 0

        if node.right:
            right_depth = node.right.depth
        else:
            right_depth = 0

        node.depth = max([left_depth, right_depth]) + 1

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

    def _delete_right_subtrees_leftmost_child(self, node, swap_node):
        """Delete node with its right subtees leftmost child."""
        if swap_node.right:
            swap_node.parent.left = swap_node.right
            swap_node.right.parent = swap_node.parent

        if swap_node.parent.left == swap_node:
            swap_node.parent.left = None
        elif swap_node.parent.right == swap_node:
            swap_node.parent.right = None

        swap_node.parent = node.parent
        swap_node.right = node.right
        if swap_node is not node.left:
            swap_node.left = node.left
            if node.left:
                node.left.parent = swap_node

        if node.right:
            node.right.parent = swap_node

        if node is not self.root:
            if node == node.parent.right:
                node.parent.right = swap_node
            if node == node.parent.left:
                node.parent.left = swap_node
        else:
            self.root = swap_node

    def _delete_left_subtrees_rightmost_child(self, node, swap_node):
        """Delete node with its left subtrees rightmost child."""
        if swap_node.left:
            swap_node.parent.right = swap_node.left
            swap_node.left.parent = swap_node.parent

        if swap_node.parent.left == swap_node:
            swap_node.parent.left = None
        elif swap_node.parent.right == swap_node:
            swap_node.parent.right = None

        swap_node.parent = node.parent
        swap_node.right = node.right
        if swap_node is not node.left:
            swap_node.left = node.left
            if node.left:
                node.left.parent = swap_node

        node.right.parent = swap_node

        if node is not self.root:
            if node == node.parent.right:
                node.parent.right = swap_node
            if node == node.parent.left:
                node.parent.left = swap_node
        else:
            self.root = swap_node


class AVLBST(BinarySearchTree):
    """Self balancing binary search tree."""

    def __init__(self, val=None):
        """Initialize avlbst."""
        super(AVLBST, self).__init__(val)

    def insert(self, val):
        """Inherit method from superclass."""
        super(AVLBST, self).insert(val)
        node = self.search(val)
        self._balance_tree(node)

    def search(self, val):
        """Inherit method from superclass."""
        return super(AVLBST, self).search(val)

    def size(self):
        """Inherit method from superclass."""
        return super(AVLBST, self).size()

    def depth(self):
        """Inherit method from superclass."""
        return super(AVLBST, self).depth()

    def contains(self, val):
        """Inherit method from superclass."""
        return super(AVLBST, self).contains(val)

    def balance(self, node=None):
        """Inherit method from superclass."""
        return super(AVLBST, self).balance(node)

    def in_order(self):
        """Inherit method from superclass."""
        return super(AVLBST, self).in_order()

    def pre_order(self):
        """Inherit method from superclass."""
        return super(AVLBST, self).pre_order()

    def post_order(self):
        """Inherit method from superclass."""
        return super(AVLBST, self).post_order()

    def breadth_first(self):
        """Inherit method from superclass."""
        return super(AVLBST, self).breadth_first()

    def delete(self, val):
        """Inherit method from superclass."""
        try:
            node = self.search(val).parent
        except AttributeError:
            return
        super(AVLBST, self).delete(val)
        self._balance_tree(node)

    def _balance_tree(self, node):
        """Balance entire tree from a starting node up to root."""
        while node:
            self._balance_node(node)
            node = node.parent

    def _balance_node(self, node):
        """Balance on a node."""
        node_balance = self.balance(node)

        if node_balance == -2:
            child_balance = self.balance(node.right)

            if child_balance == 1:
                self._right_rotation(node.right)
                self._left_rotation(node)

            if child_balance == -1:
                self._left_rotation(node)

        if node_balance == 2:
            child_balance = self.balance(node.left)

            if child_balance == -1:
                self._left_rotation(node.left)
                self._right_rotation(node)

            if child_balance == 1:
                self._right_rotation(node)

    def _right_rotation(self, node):
        """Right rotation."""
        pivot = node.left
        node.left = pivot.right

        if pivot.right:
            pivot.right.parent = node

        pivot.parent = node.parent

        if node is self.root:
            self.root = pivot
        else:
            if node.parent.left is node:
                node.parent.left = pivot
            else:
                node.parent.right = pivot

        pivot.right = node
        node.parent = pivot

        self._rebalance_node(node)
        self._rebalance_node(pivot)

    def _left_rotation(self, node):
        """Left rotation."""
        pivot = node.right
        node.right = pivot.left

        if pivot.left:
            pivot.left.parent = node

        pivot.parent = node.parent

        if node is self.root:
            self.root = pivot
        else:
            if node.parent.left is node:
                node.parent.left = pivot
            else:
                node.parent.right = pivot

        pivot.left = node
        node.parent = pivot

        self._rebalance_node(node)
        self._rebalance_node(pivot)

    def _rebalance_node(self, node):
        """Rebalance a node based on its children."""
        if node.left:
            left_depth = node.left.depth
        else:
            left_depth = 0

        if node.right:
            right_depth = node.right.depth
        else:
            right_depth = 0

        node.depth = max([left_depth, right_depth]) + 1


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
