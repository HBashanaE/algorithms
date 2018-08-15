# Shortest Paths

## Bellman-Ford Algorithm

Bellman-Ford Algorithm implementation for a graph represented with an edge list. Returns empty list if contains a negative cycle. Tested on below graphs.

![Shortest Paths](../README/shortest-paths-2.png)

![Negative Cycles](../README/shortest-paths-3.png)

**File: `a_bellman_ford.py`**

## Dijkstra Algorithm

Dijkstra Algorithm implementation for a graph represented with an adjacent list.  Gives wrong answer if given a graph with negative weights. Includes both normal and `heapq` implementation. Tested on above first graph.

**File: `b_dijkstra.py`**

## Floyd-Warshall Algorithm

Floyd-Warshall Algorithm implementation for a graph represented with an adjacent list.  Gives wrong answer if given a graph with negative weights. Tested on above first graph.

**File: `c_floyd_warshall.py`**

## Time Complexities

| Algorithm          | Description                               | Time Complexity |
| ------------------ | ----------------------------------------- | --------------- |
| `bellman_ford()`   | Bellman-Ford Algorithm                    | `O(nm)`         |
| `dijkstra()`       | Dijkstra Algorithm normal implementation. | `O(n^2)`        |
| `dijkstra_heapq()` | Dijkstra Algorithm `heapq` implementation | `O(n+mlogm)`    |
| `floyd_warshall()` | Floyd-Warshall Algorithm                  | `O(n^3)`        |

`n` = no of nodes

`m` = no of edges