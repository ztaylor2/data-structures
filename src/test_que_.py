"""Test queue data structure."""

import pytest

@pytest.fixture
def queue_fixture():
    """A fixture for the queue."""
    from que_ import Queue
    que = Queue()
    return que


def test_enqueue(queue_fixture):
    """."""
    queue_fixture.enqueue(5)
    assert queue_fixture.dequeue() == 5