"""Test module for the binary heap data structure."""


def test_push_method(binheap_full_sorted):
    """Test if push method is working."""
    assert binheap_full_sorted.heap_list == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]
    

def test_determine_parent_node_index_from_left_child_index_second_tier(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(1) == 0


def test_determine_parent_node_index_from_left_child_index_third_tier(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(3) == 1


def test_determine_parent_node_index_from_left_child_index_fourth_tier(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(7) == 3


def test_determine_parent_node_index_from_left_child_index_fourth_tier_fifth_node(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(11) == 5


def test_determine_parent_node_index_from_right_child_index_second_tier(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(2) == 0


def test_determine_parent_node_index_from_right_child_index_third_tier(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(4) == 1


def test_determine_parent_node_index_from_right_child_index_fourth_tier(binheap_full_sorted):
    """Test to find the index of parent from and odd index child node."""
    assert binheap_full_sorted._parent_index_from_child_index(14) == 6


def test_left_child_index_from_parent_zero(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._left_child_index_from_parent(0) == 1


def test_left_child_index_from_parent_six(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._left_child_index_from_parent(6) == 13


def test_right_child_index_from_parent_zero(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._right_child_index_from_parent(4) == 10


def test_parent_value_from_child_index_nine(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._parent_value_from_child_index(9) == 8


def test_parent_value_from_child_index_14(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._parent_value_from_child_index(14) == 6


def test_parent_value_from_child_index_three(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._parent_value_from_child_index(3) == 11


def test_parent_value_from_child_index_two(binheap_full_sorted):
    """."""
    assert binheap_full_sorted._parent_value_from_child_index(2) == 12