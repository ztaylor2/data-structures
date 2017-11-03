"""Module for creating a graph data structure."""

class Graph(object):
    """A graph data structure."""

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

    def nodes(self):
        """Retrun the nodes of the graph as a list."""
        try:
            nodes = []
            for key in self.graph:
                nodes.append(key)
            return nodes
        except KeyError:
            return None

    def edges(self):
        """Return the edges of the graph."""
        try:
            edges = []
            for key in self.graph:
                for i in self.graph[key]:
                    try:
                        pointer_back = key
                        pointer_front = i
                        edges.append((pointer_back, pointer_front))
                    except IndexError:
                        continue
            return edges
        except KeyError: # TODO need to add functionality for empty graph
            raise KeyError("The graph is empty.")
            
