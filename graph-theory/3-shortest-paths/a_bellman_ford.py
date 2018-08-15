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
        raise TypeError()
    else:
        return shortest_distances
