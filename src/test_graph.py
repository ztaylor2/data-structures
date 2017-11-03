"""Testing for graph data structure."""

import pytest


def test_graph_init(graph):
    """Test that the graph is initialized, and a dict is created on init."""
    assert isinstance(graph.graph, dict)


def test_add_node_puts_something_in_graph(graph):
    """Test that the add node function adds something to the graph."""
    graph.add_nodes(5)
    assert graph.graph != {}


def test_add_edge_adds_one_edge(graph):
    """Test that the add edge function adds one edge."""
    graph.add_nodes(5)
    graph.add_nodes(6)
    graph.add_edge(5, 6)
    assert graph.graph[5][0] == 6
