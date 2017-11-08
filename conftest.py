"""Fixtures for testing."""

import pytest


@pytest.fixture
def binheap_fixture():
    """Fixture for the binary heap data structure."""
    from binheap import Heap
    return Heap()


@pytest.fixture
def binheap_full_sorted():
    """A fully sorted binheap."""
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
    """A unsorted binheap."""
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


@pytest.fixture()
def priorityq():
    """A fixture for an empty priority queue."""
    from priorityq import PriorityQue
    priorityq = PriorityQue()
    return priorityq


@pytest.fixture()
def priorityq_5_first_pushed_no_priority():
    """A fixture for an empty priority queue."""
    from priorityq import PriorityQue
    priorityq = PriorityQue()
    priorityq.insert(5)
    priorityq.insert(6)
    priorityq.insert(7)
    priorityq.insert(8)
    priorityq.insert(9)
    return priorityq


@pytest.fixture()
def priorityq_7_last_pushed_yes_priority():
    """A fixture for an empty priority queue."""
    from priorityq import PriorityQue
    priorityq = PriorityQue()
    priorityq.insert(5, 0)
    priorityq.insert(6, 1)
    priorityq.insert(4, 1)
    priorityq.insert(7, 2)
    return priorityq


@pytest.fixture()
def graph():
    """A fixture for an empty graph."""
    from graph import Graph
    graph = Graph()
    return graph


@pytest.fixture()
def graph_7():
    """A fixture for an empty graph."""
    from graph import Graph
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('A', 'D', 2)
    g.add_edge('C', 'D', 6)
    g.add_edge('C', 'B', 4)
    g.add_edge('B', 'E', 4)
    g.add_edge('E', 'F', 2)
    return graph