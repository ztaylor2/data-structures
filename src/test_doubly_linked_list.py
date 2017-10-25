"""Test a doubly linked list."""

import pytest


@pytest.fixture
def doubly_list():
    """Return dbly linked list for testing."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    return dll


def test_node_has_attributes():
    """."""
    from doubly_linked_list import Node
    n = Node(1, None, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'next')
    assert hasattr(n, 'prev')
