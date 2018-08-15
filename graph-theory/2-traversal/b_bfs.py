import collections


def bfs_iter(graph: dict, start: int) -> set:
    """Returns all visited set."""

    visited = set()
    queue = collections.deque([start])
    while queue:
        node = queue.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.appendleft(neighbor)
    return visited


def bfs_distance(graph: dict, start: int, target: int) -> int:
    """Returns shortest between start and target. 
    If unreachable returns INF"""

    visited = set()
    queue = collections.deque([(start, 0)])
    while queue:
        node, distance = queue.pop()
        if node == target:
            return distance
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.appendleft((neighbor, distance + 1))
    return float("inf")


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
    len(bfs_iter(graph, 0)) == 5
)
assert(
    bfs_distance(graph, 0, 3) == 2
)
