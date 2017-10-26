"""Test a doubly linked list."""

import pytest


@pytest.fixture
def dll_fixture():
    """."""
    from doubly_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    return dll


def test_dll_push_one_val(dll_fixture):
    """."""
    dll_fixture.push(1)
    assert len(dll_fixture) == 1


def test_dll_push_second_val(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    assert len(dll_fixture) == 2


def test_dll_append_one_val(dll_fixture):
    """."""
    dll_fixture.append(1)
    assert dll_fixture.head.data == 1


def test_dll_append_second_val(dll_fixture):
    """."""
    dll_fixture.append(1)
    dll_fixture.append(2)
    assert len(dll_fixture) == 2


def test_dll_link_to_second_node_after_appending_three(dll_fixture):
    """."""
    dll_fixture.append(1)
    dll_fixture.append(2)
    dll_fixture.append(3)
    temp = dll_fixture.head.next.data
    assert temp == 2


def test_dll_link_to_second_node_after_pushing_three(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    temp = dll_fixture.head.next.data
    assert temp == 2


def test_dll_pop_one_value(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    assert dll_fixture.pop() == 3


def test_dll_pop_one_value_head_prev_points_to_none(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    dll_fixture.pop()
    assert dll_fixture.head.previous is None


def test_dll_len_after_pop_one_value(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    dll_fixture.pop()
    assert len(dll_fixture) == 2


def test_dll_previous_pointer_working_with_push(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    assert dll_fixture.head.next.previous.data == 3


def test_dll_shift_removes_correct_value(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    assert dll_fixture.shift() == 1


def test_dll_shift_modifies_length(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    dll_fixture.shift()
    assert len(dll_fixture) == 2


def test_dll_shift_tail_points_to_none(dll_fixture):
    """."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    dll_fixture.shift()
    assert dll_fixture.tail.next is None