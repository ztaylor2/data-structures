"""Test a doubly linked list."""

import pytest


@pytest.fixture
def doubly_list():
    """Return dbly linked list for testing."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    return dll
