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


def list_components(graph: dict) -> list:
    """Lists all components in a graph using DFS"""

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
