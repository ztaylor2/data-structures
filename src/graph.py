"""Module for creating a graph data structure."""
from que_ import Queue


class Graph(object):
    """A graph data structure."""

    def __init__(self):
        """Initialize the graph as a dictionary."""
        self.graph = {}

    def add_nodes(self, val):
        """Add a new node with input val to the graph."""
        self.graph[val] = {}

    def add_edge(self, val1, val2, weight):
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
        self.graph[val1].update({val2: weight})

    def nodes(self):
        """Return the nodes of the graph as a list."""
        try:
            nodes = []
            for key in self.graph:
                nodes.append(key)
            return sorted(nodes)
        except KeyError:
            return None

    def edges(self):
        """Return the edges and their weight of the graph."""
        edges = []
        for key in self.graph:
            for val in self.graph[key].items():
                try:
                    pointer_back = key
                    pointer_front = val[0]
                    weight = val[1]
                    edges.append((pointer_back, pointer_front, weight))
                except IndexError:
                    continue
        if edges == []:
            raise KeyError("Cannot return edges of empty graph.")
        else:
            return edges

    def del_edge(self, val1, val2):
        """Delete the edge connecting val1 to val2."""
        if val1 in self.graph and val2 in self.graph:
            try:
                del(self.graph[val1][val2])
            except KeyError:
                raise KeyError("{} and {} are not connected.".format(val1, val2))
        else:
            if val1 not in self.graph and val2 not in self.graph:
                raise KeyError("{} {} are not nodes.".format(val1, val2))
            elif val1 not in self.graph:
                raise KeyError("{} is not a node.".format(val1))
            else:
                raise KeyError("{} is not a node.".format(val2))

    def del_node(self, val):
        """Delete a node from the graph."""
        try:
            for key in self.graph:
                if val in self.graph[key]:
                    self.del_edge(key, val)
            del(self.graph[val])
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
        """Return the neighbors of the node connect by an edge and their weight."""
        try:
            return self.graph[val]
        except KeyError:
            raise KeyError("{} is not in the graph.".format(val))

    def adjacent(self, val1, val2):
        """Check if there is an edge between two specified nodes."""
        if val2 in self.graph[val1]:
            return True
        elif val1 in self.graph[val2]:
            return True
        elif val1 not in self.graph and val2 not in self.graph:
            raise KeyError("Neither value in graph.")
        else:
            return False

    def breadth_first_traversal(self, val):
        """
        Perform a breadth first traversal.

        The breadth first traversal starts at the user input val
        and explores the neighbor nodes first before moving on to
        the next depth of neighbors.
        """
        search_order = []
        children_queue = Queue()
        children_queue.enqueue(val)
        while children_queue.peek():
            if self.graph[children_queue.peek()] == {}:
                child = children_queue.dequeue()
                if child not in search_order:
                    search_order.append(child)
            else:
                for child in self.graph[children_queue.peek()].keys():
                    if child not in search_order:
                        children_queue.enqueue(child)
                search_order.append(children_queue.dequeue())
        return search_order

    def depth_first_traversal(self, val):
        """
        Perform a depth first traversal.

        The depth first traversal continues exploring next node at the next
        depth until the end of the branch is reached. It will then start from
        the top and continue down any other branches.
        """
        if val not in self.graph:
            raise KeyError("{} not in graph.".format(val))
        discovered = []

        def _handle_depth_first_traversal(val):
            """Helper furnction, allow for recursion w/out redefining discovered list."""
            discovered.append(val)
            if self.graph[val] != {}:
                for i in self.graph[val].keys():
                    if i not in discovered:
                        _handle_depth_first_traversal(i)
            return discovered
        return _handle_depth_first_traversal(val)

    def dijkstra(self, start, target):
        """Djikstas algorithm to determine shortest path."""

        visited = []
        # set or dict of nodes and distances (starting at inf.)

        # check childred of start nodes and assign their distances to dict

        # set current to node not in visited with the shortest distance

        while current is not target:
            # check children of current
            # if distance to child is shorter than current distance in dict
                # replace distance

            # set current to node not in visited with shortest distance assigned to it


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('A', 'D', 2)
    g.add_edge('C', 'D', 6)
    g.add_edge('C', 'B', 4)
    print("breadth first: {}".format(g.breadth_first_traversal('A')))
    print("depth first: {}".format(g.depth_first_traversal('A')))
