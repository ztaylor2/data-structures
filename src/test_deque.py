"""Testing deque data structure."""

import pytest



@pytest.fixture
def deque():
    """A fixture for the queue."""
    from deque import Deque
    return Queue()


def test_append_method(deque):
    """Test the append method."""
    deque.append(5)
    assert deque.tail.data == 5


def test_append_left(deque):
    """Test the append left method."""
    deque.appendleft(5)
    assert deque.head.data == 5
