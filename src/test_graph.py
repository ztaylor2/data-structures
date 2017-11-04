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
    assert graph.nodes() == [1, 2, 9, 10]


def test_return_edges(graph):
    """Test that the edges method returns a list of all edges."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    assert sorted(graph.edges()) == [(1, 2), (1, 10), (9, 10)]


def test_graph_raises_key_error_when_check_edges_of_empty_graph(graph):
    """."""
    with pytest.raises(KeyError):
        graph.edges()


def test_delete_edge_one_edge(graph):
    """Test that deleting an edge deletes one added edge."""
    graph.add_edge(1, 2)
    assert graph.edges() == [(1, 2)]
    graph.del_edge(1, 2)
    with pytest.raises(KeyError):
        graph.edges()


def test_delete_edge_when_no_edges(graph):
    """Test that deleting an edge with no edge raises error."""
    with pytest.raises(KeyError):
        graph.del_edge(1, 2)


def test_delete_edge_when_not_edge(graph):
    """Test that deleting an edge with node but no edge raises index error."""
    graph.add_nodes(1)
    with pytest.raises(KeyError):
        graph.del_edge(1, 2)


def test_del_node(graph):
    """Test that the node is deleted from graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    graph.del_node(1)
    graph.del_node(9)
    assert graph.nodes() == [2, 10]


def test_del_node_removes_edges(graph):
    """Test if nodes are deleted their corresponding edges are deleted too."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    graph.del_node(10)
    assert graph.graph == {1: [2], 2: [], 9: []}


def test_del_node_raises_error(graph):
    """Test that proper error message is raised when deleting empty graph."""
    with pytest.raises(IndexError):
        graph.del_node(5)


def test_has_node_true(graph):
    """Test that the node is in the graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    graph.del_node(10)
    assert graph.has_node(1) is True


def test_has_node_false(graph):
    """Test that the node is not in the graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    graph.del_node(10)
    assert graph.has_node(99) is False


def test_has_node_error(graph):
    """Test that the node is in the graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    graph.del_node(10)
    assert graph.has_node(99) is False


def test_neighbors(graph):
    """Test that neighbors function returns the nodes that val is connected with."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    assert graph.neighbors(1) == [2, 10]


def test_adjacent_true(graph):
    """Test the adjacent function."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    assert graph.adjacent(1, 10) is True


def test_adjacent_false(graph):
    """Test the adjacent function."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    assert graph.adjacent(2, 10) is False


def test_adjacent_error(graph):
    """Test the adjacent function."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2)
    graph.add_edge(9, 10)
    graph.add_edge(1, 10)
    with pytest.raises(KeyError):
        graph.adjacent(1, 99)