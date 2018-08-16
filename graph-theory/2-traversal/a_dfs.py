def dfs_recursion(graph: dict, current: int, visited: set) -> set:
    """Recursive implementation.
    Not suitable for larger graphs.
    Should provide empty visited set.
    Returns all visited set.
    Graph has to be passed as an adjacency list."""

    visited.add(current)
    for node in graph[current]:
        if node not in visited:
            dfs_recursion(graph, node, visited)
    return visited


def dfs_iter(graph: dict, start: int) -> set:
    """Iterative implementation. Returns all visited set.
    Graph has to be passed as an adjecency list."""

    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited
