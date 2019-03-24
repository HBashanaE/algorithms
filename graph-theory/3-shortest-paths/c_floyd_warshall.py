import collections
# **** FOR A HUGE speed boost, use PyPy as interpreter
def floyd_warshall(graph: collections.defaultdict, nodes: int):
    # Construct initial distance grid so distance from and to same node is 0
    # and weights are included
    distances = [[
        0 if a==b else (
            graph[a][b] if b in graph[a] else None
        ) 
        for b in range(nodes)] 
    for a in range(nodes)]

    # Take each node as intermediate node
    for intermediate_node in range(nodes):
        # Take each node as node A
        for node_a in range(nodes):
            if distances[node_a][intermediate_node] == None:
                continue
            # Take each node as node B
            for node_b in range(nodes):
                if distances[intermediate_node][node_b] == None:
                    continue
                # If distance from [node A -> intermediate node -> node B]
                # is greater than [node A -> node B] save that distance
                new_distance = distances[node_a][intermediate_node] + \
                    distances[intermediate_node][node_b]
                if distances[node_a][node_b] == None:
                    distances[node_a][node_b] = new_distance
                elif distances[node_a][node_b] > new_distance:
                    distances[node_a][node_b] = new_distance

    return distances
