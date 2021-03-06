"""Test binary search tree."""

import pytest
from bst import BinarySearchTree
import random


@pytest.fixture
def bst():
    """Binary search tree."""
    return BinarySearchTree()


@pytest.fixture
def five_bst():
    """Binary search tree with root value of 5."""
    return BinarySearchTree(5)


@pytest.fixture
def full_bst():
    """Binary search tree with root value of 8."""
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


@pytest.fixture
def five_four_three_six_seven():
    """BST.
            5
        4       6
       3          7
    ."""
    bst = BinarySearchTree(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)
    return bst


@pytest.fixture
def five_four_three_two_six_seven_eight():
    """BST.
             5
         4       6
        3          7
       2             8
    ."""
    bst = BinarySearchTree(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    return bst


@pytest.fixture
def five_four_three_threefive_six_seven_sixfive():
    """BST.
                5
            4       6
         3             7
          3.5       6.5
    ."""
    bst = BinarySearchTree(5)
    bst.insert(4)
    bst.insert(3)
    bst.insert(3.5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(6.5)
    return bst


@pytest.fixture
def five_three_four_seven_six():
    """BST.
             5
         3       7
          4     6
    ."""
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    return bst


@pytest.fixture
def five_balanced():
    """BST.
              5
          3       7
        2  4     6  8
    ."""
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    return bst


@pytest.fixture
def five_right():
    """BST.
              5
          3       7
        2  4
    ."""
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    bst.insert(7)
    return bst


@pytest.fixture
def five_left():
    """BST.
              3
           2     5
                4  7
    ."""
    bst = BinarySearchTree(3)
    bst.insert(2)
    bst.insert(5)
    bst.insert(4)
    bst.insert(7)
    return bst


def test_root_node_on_init(five_bst):
    """Test that the root node exists on init."""
    assert five_bst.root.val == 5


def test_root_node_none():
    """Test that the root node is none if no value put in."""
    bst = BinarySearchTree()
    assert not bst.root


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
    """Test search method returns none if the value searched isn't in tree."""
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


# def test_depth_helper_function(full_bst):
#     """Test the depth helper function."""
#     full_bst._depth_fxn(full_bst.root, 1)
#     assert full_bst.depths_list == [4]


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
    """Test an unbalanced tree returns negative one right has more depth."""
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


def test_in_order_traversal_iterate(full_bst):
    """Test in order iterate traversal method of bst."""
    bf = full_bst._in_order_iterate()
    assert next(bf) == 1
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8
    assert next(bf) == 10
    assert next(bf) == 13
    assert next(bf) == 14

# Recursive method only works in python 3

# def test_in_order_traversal_recurse(full_bst):
#     """Test in order traversal recursive method of bst."""
#     bf = full_bst.in_order('recurse')
#     assert next(bf) == 1
#     assert next(bf) == 3
#     assert next(bf) == 4
#     assert next(bf) == 6
#     assert next(bf) == 7
#     assert next(bf) == 8
#     assert next(bf) == 10
#     assert next(bf) == 13
#     assert next(bf) == 14


def test_in_order_empty_error():
    """Test that in order traversal throws index error when empty tree."""
    bst = BinarySearchTree()
    bst_traversal = bst.in_order()
    with pytest.raises(StopIteration):
        next(bst_traversal)


def test_pre_order_traversal(full_bst):
    """Test pre order traversal method of bst."""
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


def test_pre_order_traversal_iterate(full_bst):
    """Test pre order iterate traversal method of bst."""
    bf = full_bst._pre_order_iterate()
    assert next(bf) == 8
    assert next(bf) == 3
    assert next(bf) == 1
    assert next(bf) == 6
    assert next(bf) == 4
    assert next(bf) == 7
    assert next(bf) == 10
    assert next(bf) == 14
    assert next(bf) == 13

# Recursive method only works in python 3

# def test_pre_order_traversal_recurse(full_bst):
#     """Test pre order traversal recursive method of bst."""
#     bf = full_bst.pre_order('recurse')
#     assert next(bf) == 8
#     assert next(bf) == 3
#     assert next(bf) == 1
#     assert next(bf) == 6
#     assert next(bf) == 4
#     assert next(bf) == 7
#     assert next(bf) == 10
#     assert next(bf) == 14
#     assert next(bf) == 13


def test_pre_order_empty_error():
    """Test that pre order traversal throws index error when empty tree."""
    bst = BinarySearchTree()
    bst_traversal = bst.pre_order()
    with pytest.raises(IndexError):
        next(bst_traversal)


def test_post_order_traversal(full_bst):
    """Test post order traversal of bst."""
    bf = full_bst.post_order()
    assert next(bf) == 1
    assert next(bf) == 4
    assert next(bf) == 7
    assert next(bf) == 6
    assert next(bf) == 3
    assert next(bf) == 13
    assert next(bf) == 14
    assert next(bf) == 10
    assert next(bf) == 8


def test_post_order_traversal_iterate(full_bst):
    """Test post order iteration traversal of bst."""
    bf = full_bst._post_order_iterate()
    assert next(bf) == 1
    assert next(bf) == 4
    assert next(bf) == 7
    assert next(bf) == 6
    assert next(bf) == 3
    assert next(bf) == 13
    assert next(bf) == 14
    assert next(bf) == 10
    assert next(bf) == 8

# Recursive method only works in python 3


# def test_post_order_traversal_recurse(full_bst):
#     """Test post order traversal recursive method of bst."""
#     bf = full_bst.post_order('recurse')
#     assert next(bf) == 1
#     assert next(bf) == 4
#     assert next(bf) == 7
#     assert next(bf) == 6
#     assert next(bf) == 3
#     assert next(bf) == 13
#     assert next(bf) == 14
#     assert next(bf) == 10
#     assert next(bf) == 8


def test_post_order_empty_error():
    """Test that post order traversal throws index error when empty tree."""
    bst = BinarySearchTree()
    bst_traversal = bst.post_order()
    with pytest.raises(StopIteration):
        next(bst_traversal)


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


def test_breadth_first_order_empty_error():
    """Test that post order traversal throws index error when empty tree."""
    bst = BinarySearchTree()
    bst_traversal = bst.breadth_first()
    with pytest.raises(IndexError):
        next(bst_traversal)


def test_bst_delete_leaf(full_bst):
    """Test bst delete method deletes leaf node."""
    full_bst.delete(1)
    bf = full_bst.in_order()
    assert next(bf) == 3
    assert not full_bst.contains(1)


def test_bst_delete_leaf_pointers_reassigned(full_bst):
    """Test bst delete method reassignes pointers."""
    full_bst.delete(1)
    assert not full_bst.root.left.left


def test_bst_delete_one_child_left(full_bst):
    """Test bst deletes a node with one child (left)."""
    full_bst.delete(14)
    bf = full_bst.in_order()
    assert next(bf) == 1
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8
    assert next(bf) == 10
    assert next(bf) == 13


def test_bst_delete_one_child_right(full_bst):
    """Test bst deletes a node with one child (right)."""
    full_bst.delete(10)
    bf = full_bst.in_order()
    assert next(bf) == 1
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8
    assert next(bf) == 13
    assert next(bf) == 14


def test_bst_delete_one_child_left_left(five_four_three_six_seven):
    """Test bst deletes a node with one child (left)."""
    five_four_three_six_seven.delete(4)
    bf = five_four_three_six_seven.in_order()
    assert next(bf) == 3
    assert next(bf) == 5
    assert next(bf) == 6
    assert next(bf) == 7


def test_bst_delete_one_child_left_right(five_three_four_seven_six):
    """Test bst deletes a node with one child (right)."""
    five_three_four_seven_six.delete(3)
    bf = five_three_four_seven_six.in_order()
    assert next(bf) == 4
    assert next(bf) == 5
    assert next(bf) == 6
    assert next(bf) == 7


def test_bst_delete_one_child_right_right(five_four_three_six_seven):
    """Test bst deletes a node with one child (left)."""
    five_four_three_six_seven.delete(6)
    bf = five_four_three_six_seven.in_order()
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 5
    assert next(bf) == 7


def test_bst_delete_one_child_right_left(five_three_four_seven_six):
    """Test bst deletes a node with one child (right)."""
    five_three_four_seven_six.delete(3)
    bf = five_three_four_seven_six.in_order()
    assert next(bf) == 4
    assert next(bf) == 5
    assert next(bf) == 6
    assert next(bf) == 7


def test_find_left_subtree_rightmost_child(full_bst):
    """Test find left subtree right most child returns correct node."""
    assert full_bst._find_left_subtree_rightmost_child(full_bst.root).val == 7


def test_find_right_subtree_leftmost_child(full_bst):
    """Test find right subtree lefmost child returns corrent node."""
    assert full_bst._find_right_subtree_leftmost_child(full_bst.root).val == 10


def test_delete_decrements_size_count(five_balanced):
    """Test that after a node is deleted the size of the BST correct."""
    assert five_balanced.size() == 7
    five_balanced.delete(2)
    assert five_balanced.size() == 6


def test_delete_when_not_in_tree(five_balanced):
    """Test delete when val not in tree."""
    assert five_balanced.delete(100) is None


def test_delete_equal_length_subtrees(five_balanced):
    """Test delete on balanced tree."""
    five_balanced.delete(3)
    assert not five_balanced.contains(3)
    bf = five_balanced.in_order()
    assert next(bf) == 2
    assert next(bf) == 4
    assert next(bf) == 5
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8


def test_delete_root_node(five_balanced):
    """Test delete root node."""
    five_balanced.delete(5)
    assert not five_balanced.contains(5)
    bf = five_balanced.in_order()
    assert next(bf) == 2
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8


def test_delete_right_subtree_greater_swap_node_no_children(five_balanced):
    """Test delete."""
    five_balanced.insert(7.5)
    five_balanced.insert(8.5)
    five_balanced.delete(7)
    bf = five_balanced.in_order()
    assert next(bf) == 2
    assert next(bf) == 3
    assert next(bf) == 4
    assert next(bf) == 5
    assert next(bf) == 6
    assert next(bf) == 7.5
    assert next(bf) == 8
    assert next(bf) == 8.5


def test_delete_right_subtree_greater_depth(full_bst):
    """Test delete right subtree greater depth and swap node has child."""
    full_bst.delete(3)
    bf = full_bst.in_order()
    assert next(bf) == 1
    assert next(bf) == 4
    assert next(bf) == 6
    assert next(bf) == 7
    assert next(bf) == 8
    assert next(bf) == 10
    assert next(bf) == 13
    assert next(bf) == 14


def test_delete_left_subtree_greater_depth(full_bst):
    """Test delete right subtree greater depth and swap node has child."""
    full_bst.insert(4.5)
    full_bst.insert(3.5)
    full_bst.insert(4.25)
    full_bst.delete(6)
    bf = full_bst.in_order()
    assert next(bf) == 1
    assert next(bf) == 3
    assert next(bf) == 3.5
    assert next(bf) == 4
    assert next(bf) == 4.25
    assert next(bf) == 4.5
    assert next(bf) == 7
    assert next(bf) == 8
    assert next(bf) == 10
    assert next(bf) == 13
    assert next(bf) == 14

# moved these methods into self balancing tree class.

# def test_right_rotation(five_right):
#     """Test right rotation on simple tree on root node."""
#     five_right._right_rotation(five_right.root)
#     assert five_right.root.val == 3
#     assert five_right.root.right.val == 5
#     assert five_right.root.right.right.val == 7
#     assert five_right.root.right.left.val == 4
#     assert five_right.root.left.val == 2


# def test_right_rotation_non_root(five_four_three_two_six_seven_eight):
#     """Test right rotation on non root node."""
#     five_four_three_two_six_seven_eight._right_rotation(five_four_three_two_six_seven_eight.root.left)
#     assert five_four_three_two_six_seven_eight.root.val == 5
#     assert five_four_three_two_six_seven_eight.root.left.val == 3
#     assert five_four_three_two_six_seven_eight.root.left.left.val == 2
#     assert five_four_three_two_six_seven_eight.root.left.right.val == 4
#     assert five_four_three_two_six_seven_eight.root.right.val == 6
#     assert five_four_three_two_six_seven_eight.root.right.right.val == 7
#     assert five_four_three_two_six_seven_eight.root.right.right.right.val == 8


# def test_left_rotation(five_left):
#     """Test left rotation on simple tree on root node."""
#     five_left._left_rotation(five_left.root)
#     assert five_left.root.val == 5
#     assert five_left.root.right.val == 7
#     assert five_left.root.left.val == 3
#     assert five_left.root.left.left.val == 2
#     assert five_left.root.left.right.val == 4


# def test_left_rotation_non_root(five_four_three_two_six_seven_eight):
#     """Test left rotation on non root node."""
#     five_four_three_two_six_seven_eight._left_rotation(five_four_three_two_six_seven_eight.root.right)
#     assert five_four_three_two_six_seven_eight.root.val == 5
#     assert five_four_three_two_six_seven_eight.root.left.val == 4
#     assert five_four_three_two_six_seven_eight.root.left.left.val == 3
#     assert five_four_three_two_six_seven_eight.root.left.left.left.val == 2
#     assert five_four_three_two_six_seven_eight.root.right.val == 7
#     assert five_four_three_two_six_seven_eight.root.right.right.val == 8
#     assert five_four_three_two_six_seven_eight.root.right.left.val == 6


# def test_balance_node_neg_two_neg_one_left_rotation(five_four_three_two_six_seven_eight):
#     """Test balance node function on format of node.right.right."""
#     five_four_three_two_six_seven_eight._balance_node(five_four_three_two_six_seven_eight.root.right)
#     assert five_four_three_two_six_seven_eight.root.right.val == 7
#     assert five_four_three_two_six_seven_eight.root.right.right.val == 8
#     assert five_four_three_two_six_seven_eight.root.right.left.val == 6


# def test_balance_node_two_one_right_rotation(five_four_three_two_six_seven_eight):
#     """Test balance node funciton on format of node.left.left."""
#     five_four_three_two_six_seven_eight._balance_node(five_four_three_two_six_seven_eight.root.left)
#     assert five_four_three_two_six_seven_eight.root.left.val == 3
#     assert five_four_three_two_six_seven_eight.root.left.right.val == 4
#     assert five_four_three_two_six_seven_eight.root.left.left.val == 2


# def test_balance_node_neg_two_one_right_left_rotation(five_four_three_threefive_six_seven_sixfive):
#     """Test balance node funciton on format of node.right.left."""
#     five_four_three_threefive_six_seven_sixfive._balance_node(five_four_three_threefive_six_seven_sixfive.root.right)
#     assert five_four_three_threefive_six_seven_sixfive.root.right.val == 6.5
#     assert five_four_three_threefive_six_seven_sixfive.root.right.left.val == 6
#     assert five_four_three_threefive_six_seven_sixfive.root.right.right.val == 7


# def test_balance_node_two_neg_one_left_right_rotation(five_four_three_threefive_six_seven_sixfive):
#     """Test balance node funcitno on format of node.left.rihgt."""
#     five_four_three_threefive_six_seven_sixfive._balance_node(five_four_three_threefive_six_seven_sixfive.root.left)
#     assert five_four_three_threefive_six_seven_sixfive.root.left.val == 3.5
#     assert five_four_three_threefive_six_seven_sixfive.root.left.left.val == 3
#     assert five_four_three_threefive_six_seven_sixfive.root.left.right.val == 4


def test_avlbst_class_inherits_bst():
    """Test the AVLBST class inherits bst methods."""
    from bst import AVLBST
    avlbst = AVLBST()
    avlbst.insert(5)
    assert avlbst.root.val == 5


def test_avlbst_balances_on_insert_left_left():
    """Test AVLBST balances itself on insert two left."""
    from bst import AVLBST
    avl = AVLBST()
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    assert avl.root.val == 4
    assert avl.root.right.val == 5
    assert avl.root.left.val == 3


def test_avlbst_balances_on_insert_left_right():
    """Test tree self balances with left right rotation."""
    from bst import AVLBST
    avl = AVLBST()
    avl.insert(5)
    avl.insert(3)
    avl.insert(4)
    assert avl.root.val == 4
    assert avl.root.right.val == 5
    assert avl.root.left.val == 3


def test_avlbst_balances_on_insert_right_left():
    """Test tree self balances with right left rotation."""
    from bst import AVLBST
    avl = AVLBST()
    avl.insert(5)
    avl.insert(7)
    avl.insert(6)
    assert avl.root.val == 6
    assert avl.root.right.val == 7
    assert avl.root.left.val == 5


def test_avlbst_balances_on_insert_right_right():
    """Test tree self balances with a left rotation."""
    from bst import AVLBST
    avl = AVLBST()
    avl.insert(5)
    avl.insert(6)
    avl.insert(7)
    assert avl.root.val == 6
    assert avl.root.right.val == 7
    assert avl.root.left.val == 5


def test_avlbst_delete_method_balances():
    """Test tree is balanced after delete method."""
    from bst import AVLBST
    avl = AVLBST()
    avl.insert(5)
    avl.insert(3)
    avl.insert(2)
    avl.insert(7)
    avl.delete(7)
    assert avl.root.val == 3
    assert avl.root.right.val == 5
    assert avl.root.left.val == 2


def test_insert_items_rebal_right_left_rotation():
    """Test that the tree rebalances on a left right rotation."""
    from bst import AVLBST
    avl = AVLBST()
    avl.insert(85)
    avl.insert(2)
    avl.insert(88)
    avl.insert(79)
    avl.insert(55)
    assert avl.root.val == 85
    assert avl.root.right.val == 88
    assert avl.root.left.val == 55
    assert avl.root.left.left.val == 2
    assert avl.root.left.right.val == 79
    avl.insert(50)
    assert avl.balance() == 1 or avl.balance() == 0 or avl.balance() == -1
    assert avl.root.val == 55


def test_tree_balance_returns_correctly():
    """Test balance function returns currect balance."""
    from bst import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(85)
    bst.insert(55)
    bst.insert(88)
    bst.insert(2)
    bst.insert(79)
    bst.insert(50)
    assert bst.balance() == 2


def test_depth_function_returns_correctly():
    """Test that the depth function returns correct val."""
    from bst import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(85)
    bst.insert(55)
    bst.insert(88)
    bst.insert(2)
    bst.insert(79)
    bst.insert(50)
    assert bst.depth() == 4


def test_node_depth_attribute_updates():
    """Test the node depth attribute is accurate."""
    from bst import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(5)
    assert bst.root.depth == 1
    bst.insert(6)
    assert bst.root.depth == 2
    bst.insert(7)
    assert bst.root.depth == 3


def test_insert_many_times_balance():
    """Test self balancing tree still balanced after 50 random insertions."""
    from bst import AVLBST
    avl = AVLBST()
    for _ in range(50):
        random_int = random.randint(1, 1000)
        avl.insert(random_int)
    assert avl.balance() == 1 or avl.balance() == 0 or avl.balance() == -1


# def test_insert_many_times_delete_many_times():
#     """Test that inserting then deleting many times results in balanced tree."""
#     from bst import AVLBST
#     avl = AVLBST()

#     nodes_to_delete = []

#     for _ in range(50):
#         random_int = random.randint(1, 1000)
#         # 50% chance of node being added to delete list
#         delete_probability = random.randint(1, 2)

#         if delete_probability == 1:
#             if random_int not in nodes_to_delete:
#                 nodes_to_delete.append(random_int)

#         avl.insert(random_int)

#     for val in nodes_to_delete:
#         avl.delete(val)

#     assert avl.balance() == 1 or avl.balance() == 0 or avl.balance() == -1


def test_delete_root_node_only_node(bst):
    """Test deleteing the root node."""
    bst.insert(5)
    bst.delete(5)
    assert bst.root is None


def test_delete_root_node_one_right_child(bst):
    """Test delete root node w one rihgt child."""
    bst.insert(5)
    bst.insert(6)
    bst.delete(5)
    assert bst.root.val == 6
    assert bst.root.parent is None
    assert bst.root.right is None
    assert bst.root.left is None
    assert bst.root.depth == 1


def test_delete_root_node_one_left_child(bst):
    """Test deleting root node wiht one left child."""
    bst.insert(5)
    bst.insert(4)
    bst.delete(5)
    assert bst.root.val == 4
    assert bst.root.parent is None
    assert bst.root.right is None
    assert bst.root.left is None
    assert bst.root.depth == 1


def test_delete_node_only_right_no_left_child_reassignes_depths(bst):
    """Test deleting node w node.right not node.left reassignes depths."""
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(9)
    bst.delete(7)
    assert bst.root.depth == 2
    assert bst.root.right.depth == 1
    assert bst.root.left.depth == 1


def test_delete_reassignes_depth_large_tree(bst):
    """Test delete reassignes depths correctly all the way up tree."""
    bst.insert(8)
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    assert bst.root.left.left.left.left.depth == 1
    assert bst.root.left.left.left.depth == 2
    assert bst.root.left.left.depth == 3
    assert bst.root.left.depth == 4
    assert bst.root.depth == 5
    bst.delete(2)
    assert bst.root.left.left.left.depth == 1
    assert bst.root.left.left.depth == 2
    assert bst.root.left.depth == 3
    assert bst.root.depth == 4


def test_delete_node_only_left_no_right_reassignes_depths(bst):
    """Test deleting node w node.left not node.right reassignes depths."""
    bst.insert(5)
    bst.insert(3)
    bst.insert(6)
    bst.insert(2)
    bst.delete(3)
    assert bst.root.depth == 2
    assert bst.root.left.depth == 1
    assert bst.root.right.depth == 1


def test_delete_two_children_depths_reassigned(bst):
    """Test depths get reassinged."""
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(8)
    bst.insert(6)
    bst.insert(2)
    bst.insert(4)
    bst.insert(2.5)
    bst.insert(2.75)
    bst.delete(3)
    assert bst.root.left.val == 2.75
    assert bst.root.left.depth == 3


def test_self_balancing_after_many_rotations():
    """Test all balance methods work in tandom."""
    from bst import AVLBST
    bst = AVLBST([50, 25, 15, 60, 70, 10, 12, 80, 75])
    assert bst.root.val == 60
    assert bst.root.left.val == 25
    assert bst.root.left.left.val == 12
    assert bst.root.left.left.left.val == 10
    assert bst.root.left.left.right.val == 15
    assert not bst.root.left.left.left.right
    assert not bst.root.left.left.left.left
    assert bst.root.left.right.val == 50
    assert not bst.root.left.right.right
    assert not bst.root.left.right.left
    assert bst.root.right.val == 75
    assert bst.root.right.right.val == 80
    assert not bst.root.right.right.right
    assert not bst.root.right.right.left
    assert bst.root.right.left.val == 70
    assert not bst.root.right.left.left
    assert not bst.root.right.left.right
