def bellman_ford(graph: set, nodes: int, start: int) -> list:
    """Bellman Ford Algorithm to search shortest distance from a node.
    Graph has to be passed as an edge list.
    Nodes has to be indexed 0..n.

    Time Complexity: O(nm)"""

    shortest_distances = [float("inf")]*nodes
    shortest_distances[start] = 0
    for i in range(nodes):
        changed = False
        for edge in graph:
            a, b, w = edge
            b_distance = w + shortest_distances[a]
            if b_distance < shortest_distances[b]:
                changed = True
                shortest_distances[b] = b_distance
        if not changed:
            break
    if i == nodes-1 and changed:
        # Negative cycle
        return []
    else:
        return shortest_distances


# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
graph = {
    (0, 1, 3),
    (0, 3, 5),
    (1, 4, 2),
    (1, 2, 7),
    (2, 5, 9),
    (3, 4, 4),
    (4, 5, 6)
}
negative_cycle_graph = {
    (0, 1, 5),
    (0, 2, 4),
    (1, 3, 3),
    (2, 1, -6),
    (3, 2, 2)
}
assert(
    bellman_ford(graph, nodes=6, start=0)[5] == 11
)
assert(
    bellman_ford(negative_cycle_graph, nodes=4, start=0) == []
)
