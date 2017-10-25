"""Testing a stack in python."""

import pytest


def test_stack_object():
    """Test the stack object."""
    from stack import Stack
    s = Stack()
    assert s.head is None


def test_push():
    """Test the push method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    assert s.head is not None


def test_len():
    """Test the len method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    assert len(s) == 1


def test_pop():
    """Test pop method of Stack."""
    from stack import Stack
    s = Stack()
    s.push(5)
    s.pop(5)
    assert len(s) == 0
