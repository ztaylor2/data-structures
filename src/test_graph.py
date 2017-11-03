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


def test_return_nodes(graph):
    """Test that we can return a list of all nodes."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    assert graph.nodes() == [1, 2, 10, 9]


def test_return_edges(graph):
    """Test that the edges method returns a list of all edges."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    assert graph.edges() == [(1, 2), (1, 10), (9, 10)]


def test_return_key_error_empty_graph(graph):
    """."""
    with pytest.raises(KeyError):
        graph.edges()


# def test_del_node(graph):
#     """Test that the node is deleted from graph."""
#     graph.add_nodes(1)
#     graph.add_nodes(2)
#     graph.add_edge(1, 2)
#     graph.add_edge(9, 10)
#     graph.add_edge(1, 10)
#     graph.del_node(1)
#     graph.del_node(9)
#     assert graph.nodes() == [2, 9, 10]
