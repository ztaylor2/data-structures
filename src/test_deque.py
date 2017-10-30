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


def test_pop_with_append(deque_fixture):
    """Test the functionality of pop with append."""
    deque_fixture.append(1)
    assert deque_fixture.pop() == 1

def test_pop_with_appendleft(deque_fixture):
    """Test the functionality of pop with append left method."""
    deque_fixture.appendleft(1)
    assert deque_fixture.pop() == 1

def test_pop_with_two_appends(deque_fixture):
    """Test pop after two appends."""
    deque_fixture.append(1)
    deque_fixture.append(2)
    assert deque_fixture.pop() == 2

def test_pop_with_two_appendleft(deque_fixture):
    """Test pop after two append lefts."""
    deque_fixture.appendleft(1)
    deque_fixture.appendleft(2)
    assert deque_fixture.pop() == 1


def test_popleft_with_append(deque_fixture):
    """Testing pop left with append."""
    deque_fixture.append(1)
    assert deque_fixture.popleft() == 1


def test_popleft_with_appendleft(deque_fixture):
    """Test the functionality of popleft with append left method."""
    deque_fixture.appendleft(1)
    assert deque_fixture.popleft() == 1


def test_popleft_with_two_appends(deque_fixture):
    """Test pop after two appends."""
    deque_fixture.append(1)
    deque_fixture.append(2)
    assert deque_fixture.popleft() == 1


def test_popleft_with_two_appendleft(deque_fixture):
    """Test popleft after two append lefts."""
    deque_fixture.appendleft(1)
    deque_fixture.appendleft(2)
    assert deque_fixture.pop() == 1
