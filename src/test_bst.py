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


def test_depth_returns_depth_of_tree(full_bst):
    """Test depth method returns proper depth of tree of depth four."""
    assert full_bst.depth() == 4