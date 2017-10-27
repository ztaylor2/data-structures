"""Test a doubly linked list."""

import pytest


@pytest.fixture
def doubly_list(scope="function"):
    """Return dbly linked list for testing."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    return dll


def test_node_has_attributes():
    """Test node."""
    from doubly_linked_list import Node
    n = Node(1, None, None)
    assert hasattr(n, 'data')


def test_doubly_linked_list_has_head(doubly_list):
    """Test head."""
    assert doubly_list.list.head is None


def test_doubly_linked_list_push_adds_new_item(doubly_list):
    """Test push."""
    doubly_list.push('val')
    assert doubly_list.head.data == 'val'


def test_doubly_linked_list_counter(doubly_list):
    """Test counter."""
    doubly_list.push(1)
    doubly_list.push(2)
    assert len(doubly_list) == 2


def test_doubly_linked_list_push(doubly_list):
    """Test push."""
    doubly_list.push(1)
    assert len(doubly_list) == 1


def test_doubly_linked_list_append(doubly_list):
    """Test append."""
    doubly_list.append(1)
    assert len(doubly_list) == 1


def test_doubly_linked_shift(doubly_list):
    """Test pop."""
    doubly_list.push(77)
    assert doubly_list.pop() == 77


def test_doubly_pop_and_append(doubly_list):
    """Test popping an append."""
    doubly_list.append(77)
    assert doubly_list.pop() == 77


def test_pop_when_empty_list_exception(doubly_list):
    """Test error for pop of empty list."""
    with pytest.raises(IndexError):
        doubly_list.pop()


def test_shift_returns_correct_val(doubly_list):
    """Test shift."""
    doubly_list.push(77)
    doubly_list.push(66)
    doubly_list.push(55)
    assert doubly_list.shift() == 77


def test_shift_when_empty_list_exception(doubly_list):
    """Test error for pop of empty list."""
    with pytest.raises(IndexError):
        doubly_list.shift()


def test_doubly_next_val_assign_when(doubly_list):
    """Test popping an append."""
    doubly_list.append(77)
    doubly_list.append(66)
    doubly_list.append(55)
    assert doubly_list.pop() == 77
    assert doubly_list.pop() == 66
    assert doubly_list.pop() == 55


def test_init_iterable():
    """Test for handling interable on init."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList((77, 66, 55))
    assert dll.pop() == 77
    assert dll.pop() == 66
    assert dll.pop() == 55


def test_remove_method(doubly_list):
    """Test remove method."""
    doubly_list.push(3)
    doubly_list.push(2)
    doubly_list.push(1)
    doubly_list.remove(2)
    assert doubly_list.pop() == 1
    assert doubly_list.pop() == 3


def test_remove_when_val_not_in_list(doubly_list):
    """Test error for pop of empty list."""
    with pytest.raises(ValueError):
        doubly_list.push(1)
        doubly_list.push(1)
        doubly_list.remove(2)

def test_remove_when_one_val_in_list(doubly_list):
    """Test error for pop of empty list."""
    doubly_list.push(1)
    doubly_list.remove(1)
    assert doubly_list.head == None
    assert doubly_list.tail == None

def test_pop(doubly_list):
    """Test error for pop of empty list."""
    doubly_list.push(1)
    assert doubly_list.pop() == 1