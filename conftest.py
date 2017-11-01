"""."""

import pytest


@pytest.fixture
def binheap_fixture():
    """Fixture for the binary heap data structure."""
    from binheap import Heap
    return Heap()


@pytest.fixture
def binheap_full_sorted():
    """."""
    from binheap import Heap
    binheap = Heap()
    binheap.push(12)
    binheap.push(11)
    binheap.push(10)
    binheap.push(9)
    binheap.push(8)
    binheap.push(7)
    binheap.push(6)
    binheap.push(5)
    binheap.push(4)
    binheap.push(3)
    binheap.push(2)
    binheap.push(1)
    binheap.push(0)
    binheap.push(-1)
    binheap.push(-2)
    return binheap


@pytest.fixture
def binheap_full_unsorted():
    """."""
    from binheap import Heap
    binheap = Heap()
    binheap.push(-2)
    binheap.push(8)
    binheap.push(6)
    binheap.push(11)
    binheap.push(7)
    binheap.push(4)
    binheap.push(-1)
    binheap.push(5)
    binheap.push(0)
    binheap.push(10)
    binheap.push(3)
    binheap.push(12)
    binheap.push(9)
    binheap.push(1)
    binheap.push(2)
    return binheap