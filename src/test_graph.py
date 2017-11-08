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
    graph.add_edge(5, 6, 4)
    assert graph.graph[5] == {6: 4}


def test_return_nodes(graph):
    """Test that we can return a list of all nodes."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(9, 10, 2)
    assert graph.nodes() == [1, 2, 9, 10]


def test_return_edges(graph):
    """Test that the edges method returns a list of all edges."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(9, 10, 6)
    graph.add_edge(1, 10, 2)
    assert sorted(graph.edges()) == [(1, 2, 4), (1, 10, 6), (9, 10, 6)]


def test_graph_raises_key_error_when_check_edges_of_empty_graph(graph):
    """Test that KeyError is approporiately raised."""
    with pytest.raises(KeyError):
        graph.edges()


def test_delete_edge_one_edge(graph):
    """Test that deleting an edge deletes one added edge."""
    graph.add_edge(1, 2, 4)
    assert graph.edges() == [(1, 2, 4)]
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
    graph.add_edge(1, 2, 4)
    graph.add_edge(9, 10, 99)
    graph.add_edge(1, 10, 1)
    graph.del_node(1)
    graph.del_node(9)
    assert graph.nodes() == [2, 10]


def test_del_node_removes_edges(graph):
    """Test if nodes are deleted their corresponding edges are deleted too."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 5)
    graph.add_edge(9, 10, 4)
    graph.add_edge(1, 10, 2)
    graph.del_node(10)
    assert graph.graph == {1: {2: 5}, 2: {}, 9: {}}


def test_del_node_raises_error(graph):
    """Test that proper error message is raised when deleting empty graph."""
    with pytest.raises(IndexError):
        graph.del_node(5)


def test_has_node_true(graph):
    """Test that the node is in the graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 66)
    graph.add_edge(9, 10, 40)
    graph.add_edge(1, 10, 20)
    graph.del_node(10)
    assert graph.has_node(1) is True


def test_has_node_false(graph):
    """Test that the node is not in the graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 10)
    graph.add_edge(9, 10, 20)
    graph.add_edge(1, 10, 8)
    graph.del_node(10)
    assert graph.has_node(99) is False


def test_has_node_error(graph):
    """Test that the node is in the graph."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 2)
    graph.add_edge(9, 10, 4)
    graph.add_edge(1, 10, 6)
    graph.del_node(10)
    assert graph.has_node(99) is False


def test_neighbors(graph):
    """Test that neighbors function returns the nodes that val is connected with."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 2)
    graph.add_edge(9, 10, 4)
    graph.add_edge(1, 10, 8)
    assert graph.neighbors(1) == {2: 2, 10: 8}


def test_adjacent_true(graph):
    """Test the adjacent function."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 8)
    graph.add_edge(9, 10, 4)
    graph.add_edge(1, 10, 10)
    assert graph.adjacent(1, 10) is True


def test_adjacent_false(graph):
    """Test the adjacent function."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 2)
    graph.add_edge(9, 10, 4)
    graph.add_edge(1, 10, 6)
    assert graph.adjacent(2, 10) is False


def test_adjacent_error(graph):
    """Test the adjacent function."""
    graph.add_nodes(1)
    graph.add_nodes(2)
    graph.add_edge(1, 2, 2)
    graph.add_edge(9, 10, 8)
    graph.add_edge(1, 10, 3)
    with pytest.raises(KeyError):
        graph.adjacent(1, 99)


def test_bft_output_start_root(graph_7):
    """Test the output when starting at root."""
    assert graph_7.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]


def test_bft_output_start_mid(graph_7):
    """Test the output when starting traversal in middle of tree."""
    assert graph_7.breadth_first_traversal(3) == [3, 6, 7]


def test_bft_output_start_root_point_back_up(graph_7):
    """Test the output when starting traversal in middle of tree."""
    graph_7.add_edge(6, 2)
    assert graph_7.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]
    assert graph_7.breadth_first_traversal(6) == [6, 2, 4, 5]


def test_bft_empty_graph(graph):
    """Raise error on empty graph."""
    with pytest.raises(KeyError):
        graph.breadth_first_traversal(1)


def test_dfs_output_start_root(graph_7):
    """Test the output when starting at the root."""
    assert graph_7.depth_first_traversal(1) == [1, 2, 4, 5, 3, 6, 7]


def test_dfs_output_start_mid(graph_7):
    """Test the output of depth first search when starting in the middle."""
    assert graph_7.depth_first_traversal(3) == [3, 6, 7]


def test_dfs_start_root_points_up(graph_7):
    """Test that depth first search works properly with a loop in the graph."""
    graph_7.add_edge(6, 2)
    assert graph_7.depth_first_traversal(1) == [1, 2, 4, 5, 3, 6, 7]


def test_dfs_start_mid_points_up(graph_7):
    """Depth first search works properly with a loop in the graph start mid."""
    graph_7.add_edge(6, 2)
    assert graph_7.depth_first_traversal(6) == [6, 2, 4, 5]
    assert graph_7.depth_first_traversal(1) == [1, 2, 4, 5, 3, 6, 7]


def test_dfs_empty_graph(graph):
    """Test error handiling when searching empty graph."""
    with pytest.raises(KeyError):
        graph.depth_first_traversal(1)
