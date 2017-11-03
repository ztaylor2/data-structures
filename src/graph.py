"""Module for creating a graph data structure."""

class Graph(object):
    """."""
    
    def __init__(self):
        """Initialize the graph as a dictionary."""
        self.graph = {}
    
    def add_nodes(self, val):
        """Add a new node with input val to the graph."""
        self.graph[val] = []
        
    def add_edge(self, val1, val2):
        """Add an edge from the node val1 to the node val2.
            If val1 or val2 nodes do not exist they are created."""
        try:
            self.graph[val1]
        except KeyError:
            self.add_nodes(val1)
        try:
            self.graph[val2]
        except KeyError:
            self.add_nodes(val2)
        self.graph[val1].append(val2)
        