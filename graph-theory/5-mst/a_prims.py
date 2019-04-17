import heapq


def prims_algorithms(graph: dict, root: int = 1) -> list:
    """
    Implements Prim's minimum spanning processed algorithm.
    G is assumed to be undirected.
    Returns a list of edge index forming the MST.

    Implementation detail: Best performance would be achieved
    by using a vertex heap, but such an implementation
    requires that the heap support delete functionality.
    This particular implementation uses an edge heap instead.

    returns edge list as [(v1, v2), (v2, v3), (v2, v4),...]
    This is edge list of corresponding MST
    """

    mst = []  # Minimum spanning tree
    edge_queue = []  # Priority queue - holds edges

    def add_edges_to_queue(vertex):
        """Adds all connected edges to priority queue"""
        for neighbor in graph[vertex]:
            heapq.heappush(edge_queue, (
                graph[vertex][neighbor],
                (vertex, neighbor)
            ))

    # add all connected edges of root to edge_queue
    processed = {root}
    add_edges_to_queue(root)
    while edge_queue:
        # Get next shortest edge with at least one vertex in processed
        _, edge = heapq.heappop(edge_queue)
        if edge[0] not in processed:
            v = edge[0]
        elif edge[1] not in processed:
            v = edge[1]
        else:
            continue  # Both vertices processed

        processed.add(v)
        mst.append(edge)
        add_edges_to_queue(v)
    return mst

if __name__ == "__main__":
    graph = {1: {2: 3, 3: 4}, 2: {1: 3, 4: 6, 5: 2, 3: 5},
            3: {1: 4, 2: 5, 5: 7}, 4: {2: 6}, 5: {2: 2, 3: 7}}
    assert(prims_algorithms(graph) == [(1, 2), (2, 5), (1, 3), (2, 4)])
    