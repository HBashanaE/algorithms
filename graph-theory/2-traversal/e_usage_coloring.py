def is_bipartite(graph: dict) -> bool:
    """Return whether can be colored using 2 colors.
    Uses DFS to color until it colors all or finds a neighbor with same color"""

    # Here colored dictionary acts as the visited set
    colored = {}
    # Need to store node and its color both
    stack = [(next(iter(graph.keys())), True)]
    while stack:
        # is_color_a True or False, indicating color
        node, is_color_a = stack.pop()
        colored[node] = is_color_a
        for neighbor in graph[node]:
            if neighbor not in colored:
                # Not colored
                stack.append((neighbor, not colored[node]))
            elif colored[neighbor] == colored[node]:
                # Colored in same color
                return False
    return True


# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
cycle_graph = {
    1: {2, 5},
    2: {1, 5, 3},
    3: {2, 4},
    4: {3, 5, 6},
    5: {1, 2, 4},
    6: {4}
}
no_cycle_graph = {
    1: {4},
    2: {4},
    3: {4},
    4: {1, 2, 3, 5},
    5: {4, 6},
    6: {5},
}
assert(
    not is_bipartite(cycle_graph)
)
assert(
    is_bipartite(no_cycle_graph)
)
