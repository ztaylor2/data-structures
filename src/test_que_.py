"""Test queue data structure."""

import pytest

@pytest.fixture
def queue_fixture():
    """A fixture for the queue."""
    from que_ import Queue
    que = Queue()
    return que


def test_enqueue_dequeue_one_value(queue_fixture):
    """Test enqueu one val and then dequeu it."""
    queue_fixture.enqueue(5)
    assert queue_fixture.dequeue() == 5


def test_dequeue_after_enqueu_two_vals(queue_fixture):
    """Test dequeue after two vals queued."""
    queue_fixture.enqueue(1)
    queue_fixture.enqueue(2)
    assert queue_fixture.dequeue() == 1


def test_dequeue_empty_list(queue_fixture):
    """Test that IndexError is raised when dequeing empty list."""
    with pytest.raises(IndexError):
        queue_fixture.dequeue()


def test_dequeue_second_item(queue_fixture):
    """Test two sequential dequeues."""
    queue_fixture.enqueue(1)
    queue_fixture.enqueue(2)
    queue_fixture.dequeue()
    assert queue_fixture.dequeue() == 2


def test_enqueue_mult(queue_fixture):
    """Test multiple values with enqueue."""
    queue_fixture.enqueue(1)
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    queue_fixture.enqueue(4)
    assert queue_fixture.dequeue() == 1
    assert queue_fixture.dequeue() == 2
    assert queue_fixture.dequeue() == 3
    assert queue_fixture.dequeue() == 4


def test_queue_len(queue_fixture):
    """Test len method."""
    queue_fixture.enqueue(1)
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    queue_fixture.enqueue(4)
    assert len(queue_fixture) == 4


def test_queue_peek(queue_fixture):
    """Test peek method."""
    queue_fixture.enqueue(1)
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    queue_fixture.enqueue(4)
    assert queue_fixture.peek() == 1


def test_queue_peek_does_not_mod_queue(queue_fixture):
    """Test peek method does not dequeu."""
    queue_fixture.enqueue(1)
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    queue_fixture.enqueue(4)
    queue_fixture.peek()
    assert queue_fixture.dequeue() == 1