import heapq


def dijkstra(graph:  dict, nodes: int, start: int) -> list:
    """Dijkstra Algorithm to search shortest distance from a node.
    Graph has to be passed as an adjacency list.
    Nodes has to be indexed 0..n.

    Time Complexity: O(n^2)"""

    # Set all shortest distances to INF
    shortest_distances = [float("inf")]*nodes
    # Shortest distance to start node is 0
    shortest_distances[start] = 0
    stack = [(0, start)]
    processed = set()
    # Continue until there are no items to process
    while stack:
        # Get the node with minimum shortest distance
        min_stack = min(stack)
        # Remove after taking
        stack.remove(min_stack)
        _, node = min_stack
        # If node already processed do nothing
        if node in processed:
            continue
        # Mark this node as processed
        processed.add(node)
        # Get every edge starting from this point
        for neighbor in graph[node]:
            if neighbor in processed:
                continue
            # If neighbor is not processed calculate shortest distance
            # if edge between includes in shortest path
            calculated_shortest = shortest_distances[node] + \
                graph[node][neighbor]
            # If that length is less, update shortest distance
            # and add new distance to the stack list
            if shortest_distances[neighbor] > calculated_shortest:
                shortest_distances[neighbor] = calculated_shortest
                stack.append((shortest_distances[neighbor], neighbor))
    return shortest_distances


def dijkstra_heapq(graph:  dict, nodes: int, start: int) -> list:
    """Dijkstra Algorithm to search shortest distance from a node.
    Graph has to be passed as an adjacency list.
    Nodes has to be indexed 0..n.

    Time Complexity: O(n + mlogm)"""

    # Same as above but uses heapq so that
    # adding and retrieves is O(logn) instead of O(n)
    shortest_distances = [float("inf")]*nodes
    shortest_distances[start] = 0
    # Used list but can use set without changing time complexity
    processed = [False]*nodes
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        # This is the optimized line
        _, node = heapq.heappop(heap)
        if processed[node]:
            continue
        processed[node] = True
        for neighbor in graph[node]:
            next_distance = shortest_distances[node] + graph[node][neighbor]
            if next_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = next_distance
                heapq.heappush(heap, (shortest_distances[neighbor], neighbor))
    return shortest_distances
