"""Test binary search tree."""

import pytest
from bst import BinarySearchTree


@pytest.fixture
def five_bst():
    """Binary search tree with root value of 5."""
    return BinarySearchTree(5)


@pytest.fixture
def full_bst():
    """Binary search tree with root value of 5."""
    bst = BinarySearchTree(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(14)
    bst.insert(13)
    return bst


def test_root_node_on_init(five_bst):
    """Test that the root node exists on init."""
    assert five_bst.root.val == 5


def test_root_node_none():
    """Test that the root node is none if no value put in."""
    bst = BinarySearchTree()
    assert not bst.root.val


def test_insert_adds_node(five_bst):
    """Test insert method adds a node."""
    five_bst.insert(4)
    assert five_bst.root.left.val == 4


def test_insert_adds_node_to_right(five_bst):
    """Test insert method adds a node."""
    five_bst.insert(6)
    assert five_bst.root.right.val == 6


def test_insert_multiple_adds_nodes_to_correct_spots(five_bst):
    """Test insert method adds a node."""
    five_bst.insert(6)
    five_bst.insert(7)
    five_bst.insert(8)
    assert five_bst.root.right.right.right.val == 8


def test_insert_multiple_adds_nodes_to_correct_spots_left(five_bst):
    """Test insert method adds a node."""
    five_bst.insert(4)
    five_bst.insert(3)
    five_bst.insert(2)
    assert five_bst.root.left.left.left.val == 2


def test_insert_multiple_adds_nodes_to_correct_spots_left_right(five_bst):
    """Test insert method adds a node."""
    five_bst.insert(1)
    five_bst.insert(2)
    assert five_bst.root.left.right.val == 2


def test_search_returns_something(five_bst):
    """Test search returns something."""
    assert five_bst.search(5)


def test_search_returns_node_with_correct_val(five_bst):
    """Test search returns node with correct val."""
    assert five_bst.search(5).val == 5


def test_search_returns_node_with_correct_val_full_tree(full_bst):
    """Test search returns node with correct val."""
    assert full_bst.search(6).val == 6
    assert full_bst.search(6).right.val == 7
    assert full_bst.search(6).left.val == 4


def test_search_return_none_if_val_not_in_tree(full_bst):
    """Test search method returns none if the value searched for isn't in tree."""
    assert full_bst.search(77) is None


def test_size_returns_size_of_tree_zero():
    """Test size method returns size of tree."""
    bst = BinarySearchTree()
    assert bst.size() == 0


def test_size_returns_size_of_tree_one(five_bst):
    """Test size method returns size of tree."""
    assert five_bst.size() == 1


def test_size_returns_size_of_tree(full_bst):
    """Test size method returns size of tree."""
    assert full_bst.size() == 9


def test_contains_returns_true(full_bst):
    """Test contains returns true when value is in tree."""
    assert full_bst.contains(14) is True


def test_contains_returns_false(full_bst):
    """Test contains returns false when value is in tree."""
    assert full_bst.contains(77) is False


def test_parent_pointer_works(full_bst):
    """Test the parent pointer is working."""
    assert full_bst.search(6).parent.val == 3
    assert full_bst.search(14).parent.val == 10


def test_parent_pointer_works_none(five_bst):
    """Test the parent pointer is working."""
    assert five_bst.root.parent is None


def test_depth_returns_depth_of_tree(full_bst):
    """Test depth method returns proper depth of tree of depth four."""
    assert full_bst.depth() == 4


def test_depth_returns_depth_of_tree_one(five_bst):
    """Test depth method returns proper depth of tree of depth four."""
    assert five_bst.depth() == 1


def test_depth_returns_depth_of_tree_zero():
    """Test depth method returns proper depth of tree of depth four."""
    bst = BinarySearchTree()
    assert bst.depth() == 0


def test_balance_one_val_in_tree(five_bst):
    """Test balanced tree returns zero when only one val in tree."""
    assert five_bst.balance() == 0


def test_balance_balanced_tree_full(full_bst):
    """Test balanced tree returns zero when balanced tree."""
    assert full_bst.balance() == 0


def test_unballanced_tree_one(five_bst):
    """Test an unbalanced tree returns one when left has one more depth."""
    five_bst.insert(3)
    assert five_bst.balance() == 1


def test_unballanced_tree_negative_one(five_bst):
    """Test an unbalanced tree returns negative one when right has one more depth."""
    five_bst.insert(7)
    assert five_bst.balance() == -1


def test_unballanced_tree_two(five_bst):
    """Test an unbalanced tree returns one when left has one more depth."""
    five_bst.insert(4)
    five_bst.insert(3)
    five_bst.insert(2)
    five_bst.insert(1)
    assert five_bst.balance() == 4


def test_interable_init():
    """Test init with iterable works."""
    bst = BinarySearchTree((5, 3, 6))
    assert bst.size() == 3
    assert bst.contains(5)
    assert bst.contains(3)
    assert bst.contains(6)


def test_in_order_traversal(full_bst):
    """Test in order traversal method of bst."""
    bf = full_bst.in_order()
    assert next(bf) == 1
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8
    assert next(bf) == 10
    assert next(bf) == 13
    assert next(bf) == 14


def test_pre_order_traversal(full_bst):
    """Test pre order trabersal method of bst."""
    bf = full_bst.pre_order()
    assert next(bf) == 8
    assert next(bf) == 3
    assert next(bf) == 1
    assert next(bf) == 6
    assert next(bf) == 4
    assert next(bf) == 7
    assert next(bf) == 10
    assert next(bf) == 14
    assert next(bf) == 13


def test_post_order_traversal(full_bst):
    """Test post order traversal of bst."""
    bf = full_bst.post_order()
    # assert next(bf) == 4
    # assert next(bf) == 7
    # assert next(bf) == 6
    # assert next(bf) == 1
    # assert next(bf) == 3
    # assert next(bf) == 8
    # assert next(bf) == 13
    # assert next(bf) == 10
    # assert next(bf) == 14

def test_breadth_first_traversal(full_bst):
    """Test breadth first traversal of bst."""
    bf = full_bst.breadth_first()
    assert next(bf) == 8
    assert next(bf) == 3
    assert next(bf) == 10
    assert next(bf) == 1
    assert next(bf) == 6
    assert next(bf) == 14
    assert next(bf) == 4
    assert next(bf) == 7
    assert next(bf) == 13
