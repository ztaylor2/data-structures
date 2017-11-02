"""Tests for priority queue data structure."""

import pytest


def test_priorityq_inits(priorityq):
    """Test if the priority queue exists on init."""
    assert priorityq is not None


def test_priorityq_insert_adds_a_value_and_peek_one_val(priorityq):
    """Test the insert and peek methods of priority queue with one value."""
    priorityq.insert(5)
    assert priorityq.peek() == 5


def test_peek_after_multiple_vals(priorityq_5_first_pushed_no_priority):
    """Test peek after multiple vals are added."""
    assert priorityq_5_first_pushed_no_priority.peek() == 5


def test_insert_and_pop_methods_one_val(priorityq):
    """Test insert and pop methods of priority queue with one value."""
    priorityq.insert(5)
    assert priorityq.pop() == 5


def test_pop_works_with_multiple_vals(priorityq_5_first_pushed_no_priority):
    """Test pop works after multiple values are inserted."""
    assert priorityq_5_first_pushed_no_priority.pop() == 5


def test_peek_works_with_priority(priorityq_7_last_pushed_yes_priority):
    """Test peek works when priority values are assigned on insert."""
    assert priorityq_7_last_pushed_yes_priority.peek() == 7


def test_pop_works_with_priority(priorityq_7_last_pushed_yes_priority):
    """Test pop works when priority values are assigned on insert."""
    assert priorityq_7_last_pushed_yes_priority.pop() == 7


def test_pop_after_input_of_same_priority(priorityq):
    """Test pop returns correct vals after inserting multiple vals of the same priority."""
    priorityq.insert(5, 0)
    priorityq.insert(8, 0)
    assert priorityq.pop() == 5
    assert priorityq.pop() == 8


def test_peek_after_input_of_same_priority(priorityq):
    """Test peek returns correct vals after inserting multiple vals of the same priority."""
    priorityq.insert(5, 0)
    priorityq.insert(8, 0)
    assert priorityq.peek() == 5
    assert priorityq.peek() == 5


def test_peek_throws_error_when_empty(priorityq):
    """Test that an error is thrown when trying to peek an empty queue."""
    with pytest.raises(IndexError):
        priorityq.peek()


def test_pop_throws_error_when_empty(priorityq):
    """Test that an error is thrown when trying to pop an empty queue."""
    with pytest.raises(IndexError):
        priorityq.pop()
