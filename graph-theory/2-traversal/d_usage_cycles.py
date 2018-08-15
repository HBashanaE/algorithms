def contains_cycle(graph: dict) -> bool:
    """Returns True is graph contains a cycle. Uses DFS."""

    visited = set()
    # Here we need to store both current node and the node before that
    # Because in a unidirected graph A->B->A is also possible but is not a cycle
    stack = [(next(iter(graph.keys())), None)]
    while stack:
        node, prev = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, node))
            elif neighbor != prev:
                # If node before and node after is not same
                # # and already visited node after then this is a cycle
                return True
    return False


def contains_cycle_specific(graph: dict) -> bool:
    """Returns True is graph contains a cycle.
    Uses the idea that if there isn't a cycle in a connected graph, it is a tree.
    Tree is a connected, undirected, cycleless graph.
    No of edges in a tree is n-1 where n is no of nodes
    So no of edges != n - 1 to have a cycle."""

    edges = 0
    nodes = len(graph)
    for node in graph:
        edges += len(graph[node])
    # Since this is undirected, real edges is half of this value
    real_edges = edges//2
    # If there is a cycle, m != n -1
    return real_edges != nodes - 1


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
    contains_cycle(cycle_graph)
)
assert(
    not contains_cycle(no_cycle_graph)
)
assert(
    contains_cycle_specific(cycle_graph)
)
assert(
    not contains_cycle_specific(no_cycle_graph)
)
