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
        edges = []
        for key in self.graph:
            for i in self.graph[key]:
                try:
                    pointer_back = key
                    pointer_front = i
                    edges.append((pointer_back, pointer_front))
                except IndexError:
                    continue
        if edges == []:
            raise KeyError("Cannot return edges of empty graph.")
        else:
            return edges

    def del_edge(self, val1, val2):
        """Delete the edge connecting val1 to val2."""
        try:
            self.graph[val1].remove(val2)
        except ValueError:
            try:
                if self.graph[val2]:
                    raise IndexError("{} and {} are not connected.".format(val1, val2))
            except KeyError:
                raise KeyError("{} is not a node.".format(val2))
        except KeyError:
            raise KeyError("{} is not a node.".format(val2))

    def del_node(self, val):
        """Delete a node from the graph."""
        try:
            self.graph.pop(val, None)
            for key in self.graph:
                try:
                    # import pdb; pdb.set_trace()
                    self.graph[key].remove(val)
                except ValueError:
                    continue
        except KeyError:
            raise IndexError("No such node in graph.")

    def has_node(self, val):
        """Check if node is in graph."""
        try:
            if self.graph[val]:
                return True
        except KeyError:
            return False
        
    def neighbors(self, val):
        """Return the neighbors of the node connect by an edge."""
        try:
            return self.graph[val]
        except KeyError:
            raise KeyError("{} is not in the graph.".format(val))
