"""DFS and BFS."""

a_graph = {"a": ["b"],
           "b": ["c", "d"],
           "c": ["e"],
           "d": ["a", "b"],
           "e": ["d"]}


def all_paths_dfs(start, finish):
    """Return all of the paths from start to finish."""
    paths = []

    def depth_first_traversal(current_node, path=[start]):
        """Depth first traversal."""
        for node in a_graph[current_node]:
            if node not in path:
                if node == finish:
                    paths.append(path + [node])
                depth_first_traversal(node, path + [node])

    depth_first_traversal(start)

    return paths


def all_paths_bfs(start, finish):
    """Return all of the paths from start to finish."""
    queue = [start]
    path = []
    paths = []

    while queue:
        current_node = queue.pop(0)
        path.append(current_node)
        if current_node == finish:
            paths.append(path)

        for node in a_graph[current_node]:
            queue = queue + [node]


if __name__ == '__main__':
    print(all_paths_dfs("a", "d")) # [[a, b, d], [a, b, c, e, d]]