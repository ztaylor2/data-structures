"""Testing deque data structure."""

import pytest



@pytest.fixture
def deque_fixture():
    """A fixture for the queue."""
    from deque import Deque
    return Deque()


def test_append_method(deque_fixture):
    """Test the append method."""
    deque_fixture.append(5)
    assert deque_fixture.deque.tail.data == 5


def test_append_left(deque_fixture):
    """Test the append left method."""
    deque_fixture.appendleft(5)
    assert deque_fixture.deque.head.data == 5
