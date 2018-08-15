def dfs_recursion(graph: dict, current: int, visited: set) -> set:
    """Recursive implementation.
    Not suitable for larger graphs.
    Should provide empty visited set.
    Returns all visited set."""

    visited.add(current)
    for node in graph[current]:
        if node not in visited:
            dfs_recursion(graph, node, visited)
    return visited


def dfs_iter(graph: dict, start: int) -> set:
    """Iterative implementation. Returns all visited set."""

    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited



# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
graph = {
    0: {1, 2, 4},
    1: {0, 2, 3, 4},
    2: {0, 1},
    3: {1},
    4: {0, 1},
    5: set()
}
assert(
    len(dfs_recursion(graph, 0, set())) == 5
)
assert(
    len(dfs_iter(graph, 0)) == 5
)
