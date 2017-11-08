"""Testing a stack in python."""

import pytest


def test_stack_object():
    """Test the stack object."""
    from stack import Stack
    s = Stack()
    assert s.list.head is None


def test_push():
    """Test the push method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    assert s.list.head is not None


def test_len():
    """Test the len method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    assert len(s) == 1


def test_len2():
    """Test the len method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    assert len(s) == 3


def test_pop():
    """Test pop method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    s.pop()
    assert len(s) == 0


def test_stack_can_take_iterable():
    """."""
    from stack import Stack
    a_list = [5, 2, 9, 0, 1]
    s = Stack(a_list)
    assert len(s) == 5


def test_peek():
    """."""
    from stack import Stack
    a_list = [5, 2, 9, 0, 1]
    s = Stack(a_list)
    assert s.peek() == 1
