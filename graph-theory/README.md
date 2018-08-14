# Graph Theory

## Graph Terminology

![Graph Theory Terminology](README/terminology-1.gif)

A graph consists of **nodes** and **edges**. In above graph `A, B, E, F, G, H, K and M` are nodes. All connectors are edges.

 **Path** is the way to to reach from one node to another. Path from `A to M` is `A → B → G → M`. Note that there could be more than one path between two nodes. **Simple path** is a path which does not contain same node several times in it. `A → F` is simple, but `A → B → H → A → F` is not simple.

Graph is **connected** if there is a path between any two nodes meaning that you should be able to reach another node by starting from any other node.

**Components** are each separate part of a graph. In below graph `{1, 2, 3, 4}` and `{5}` are the components of the graph.

![Disconnected Graph](README/terminology-2.jpg)

**Tree** is a *connected* graph with *n-1* nodes so there is one and only one *unique* path between any two nodes. If we take `{1, 2, 3, 4}` component of above graph as a separate graph, it would be a tree.

**Weighted graph** is a graph which has weight to every edge. Topmost Image is a weighted graph whereas above image is not. These weights can be imagined as lengths of the edges.

**Neighbor nodes or adjacent nodes** are nodes which have one edge between them. In first image `B, H and F` are neighbors of `A`.

**Degree** of a node is number of neighbors it has (or number of edges it has). So degree of `A` is 3. *Sum of degrees of a graph is `2m` where `m` is number of edges.* **Indegree** is number of incoming edges a node has. Similarly **outdegree** is number of outgoing edges. **Regular graph** is a graph in which all nodes have same degree. **Complete graph** is a graph which has `n-1` edges (meaning all nodes are connected to each other).

**Coloring** a graph means giving nodes colors so that no neighbor nodes have the same color. **Bipartite graph** is a graph which can be colored by using 2 colors. *A graph is not bipartite if and only if it contains a cycle with odd number of nodes.*

**Simple graph** is a graph which does not have edges that start and end at the same node and does not have multiple edges between two nodes.

## Graph Representation

A graph can be represented in

- Adjacency List
- Adjacency Matrix
- Edge List

## Graph Traversal

A graph can be traversed using several algorithms.

### Depth First Search Algorithm

Starts from a node and visits all nodes that can be visited from that node.

![Depth First Search](README/traversal-1.jpg)

Especially useful when,

- Simply traversing the whole graph applying some algorithm to each node
- Finding whether a graph is connected
- Finding all nodes which can be traversed from one node
- Search for a node