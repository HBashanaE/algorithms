import collections


def bfs_iter(graph: dict, start: int) -> set:
    """Returns all visited set.
    Graph has to be passed as an adjacency list."""

    visited = set()
    queue = collections.deque([start])
    while queue:
        node = queue.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.appendleft(neighbor)
    return visited


# Tested in https://www.hackerrank.com/challenges/the-quickest-way-up/problem
def bfs_distance(graph: dict, start: int, target: int):
    """Returns shortest between start and target. 
    If unreachable returns INF.
    Graph need to be unweighted.
    Graph has to be passed as an adjacency list."""

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
