def is_connected(graph: dict) -> bool:
    """Checks if this is a connected graph using DFS"""

    visited = set()
    # O(1) time complexity
    stack = [next(iter(graph.keys()))]
    while stack:
        node = stack.pop()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    # Connected if and only if no of nodes visited is same as no of all nodes
    return len(visited) == len(graph)


# Tested in https://www.hackerrank.com/challenges/torque-and-development/problem
def list_components(graph: dict) -> list:
    """Lists all components in a graph using DFS
    Will not ditect isolate nodes if they were not included using empty edge set.
    {0:set(), 1:{3,2}, 2:{3}, 3:set()} is [{0}, {1, 2, 3}]
    but
    {1:{3,2}, 2:{3}} is [{1, 2, 3}]
    So add items which are not in any components to components list
    OR always define empty edge sets as set() (Which will be inefficient in some cases)."""

    components = []
    visited = set()
    for node in graph:
        if node in visited:
            # Node already categorized
            continue
        else:
            # Node which is not categorized
            # So start from this node and categorize reachable nodes
            stack = [node]
            current_component = set()
            while stack:
                current_node = stack.pop()
                visited.add(current_node)
                current_component.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            # Add current component to components list
            components.append(current_component)
    return components
