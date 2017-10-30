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


def test_peek_after_append(deque_fixture):
    """Test peek after appending one value."""
    deque_fixture.append(1)
    assert deque_fixture.peek() == 1


def test_peek_after_two_append(deque_fixture):
    """Test peek after appending one value."""
    deque_fixture.append(2)
    deque_fixture.append(1)
    assert deque_fixture.peek() == 1


def test_peek_after_append_left(deque_fixture):
    """Test peek after appending one value to the left."""
    deque_fixture.appendleft(5)
    assert deque_fixture.peek() == 5


def test_peek_after_two_append_left(deque_fixture):
    """Test peek after appending one value to the left."""
    deque_fixture.appendleft(5)
    deque_fixture.appendleft(6)
    assert deque_fixture.peek() == 5


def test_peekleft_after_append(deque_fixture):
    """Test peekleft after appending value."""
    deque_fixture.append(5)
    assert deque_fixture.peekleft() == 5


def test_peekleft_after_two_append(deque_fixture):
    """Test peekleft after appending value."""
    deque_fixture.append(5)
    deque_fixture.append(9)
    assert deque_fixture.peekleft() == 5


def test_peekleft_after_appendleft(deque_fixture):
    """Test peekleft after appending to the left of deque."""
    deque_fixture.appendleft(7)
    assert deque_fixture.peekleft() == 7


def test_peekleft_after_two_appendleft(deque_fixture):
    """Test peekleft after appending to the left of deque."""
    deque_fixture.appendleft(7)
    deque_fixture.appendleft(8)
    assert deque_fixture.peekleft() == 8


def test_size_method(deque_fixture):
    """Test size method of deque."""
    deque_fixture.append(5)
    deque_fixture.appendleft(5)
    assert deque_fixture.size() == 2


def test_size_method_when_empty(deque_fixture):
    """Test size method of empty deque."""
    assert deque_fixture.size() == 0


def test_pop_empty_throws_error(deque_fixture):
    """Test pop empty throws error."""
    with pytest.raises(IndexError):
        deque_fixture.pop()


def test_popleft_empty_throws_error(deque_fixture):
    """Test popleft empty throws error."""
    with pytest.raises(IndexError):
        deque_fixture.popleft()


def test_peek_returns_none_if_empty(deque_fixture):
    """Test peek returns none if deque is empty."""
    assert deque_fixture.peek() is None


def test_peekleft_returns_none_if_empty(deque_fixture):
    """Test peekleft returns none if deque is empty."""
    assert deque_fixture.peekleft() is None


def test_peek_does_not_remove_node(deque_fixture):
    """Test that peek does not mutate the deque."""
    deque_fixture.append(1)
    deque_fixture.append(2)
    deque_fixture.append(3)
    deque_fixture.peek()
    assert deque_fixture.pop() == 3


def test_peekleft_does_not_remove_node(deque_fixture):
    """Test that peekleft does not mutate the deque."""
    deque_fixture.append(1)
    deque_fixture.append(2)
    deque_fixture.append(3)
    deque_fixture.peekleft()
    assert deque_fixture.popleft() == 1