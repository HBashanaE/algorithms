def floyd_warshall(graph: dict, nodes: int):
    # Construct initial distance grid so distance from and to same node is 0
    # and weights are included
    distances = [[float("inf")]*nodes for _ in range(nodes)]
    for a in graph:
        distances[a][a] = 0
        for b in graph[a]:
            distances[a][b] = graph[a][b]

    # Take each node as intermediate node
    for intermediate_node in graph:
        # Take each node as node A
        for node_a in graph:
            # Take each node as node B
            for node_b in graph:
                # If distance from [node A -> intermediate node -> node B]
                # is greater than [node A -> node B] save that distance
                new_distance = distances[node_a][intermediate_node] + \
                    distances[intermediate_node][node_b]
                if distances[node_a][node_b] > new_distance:
                    distances[node_a][node_b] = new_distance

    return distances
