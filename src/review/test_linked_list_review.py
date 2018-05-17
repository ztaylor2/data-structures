"""Test the linked list."""

import pytest


@pytest.fixture
def ll():
    """A linked list."""
    from linked_list_review import LinkedList
    return LinkedList()


def test_linked_list_push_method_empty(ll):
    """Test the linked list push method."""
    ll.push(5)
    assert ll.head.val == 5


def test_linked_list_push(ll):
    """Test pushing a bunch of numbers to the linked list."""
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    assert ll.head.val == 4
    assert ll.head.next.val == 3
    assert ll.head.next.next.val == 2
    assert ll.head.next.next.next.val == 1


def test_ll_pop(ll):
    """Test the pop method of a ll."""
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    assert ll.pop() == 4
    assert ll.head.val == 3
    assert ll.head.next.val == 2
    assert ll.head.next.next.val == 1


def test_search_ll(ll):
    """Test the search method."""
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    assert ll.search(2) == ll.head.next.next
