[TOC]

------

# Graph Theory

## Graph Terminology    

![Graph Theory Terminology](https://www.codeproject.com/KB/cpp/graphtheoryud0/main.gif) 

A graph consists of **nodes** and **edges**. In above graph `A, B, E, F, G, H, K and M` are nodes. All connectors are edges.

 **Path** is the way to to reach from one node to another. Path from `A to M` is `A → B → G → M`. Note that there could be more than one path between two nodes. **Simple path** is a path which does not contain same node several times in it. `A → F` is simple, but `A → B → H → A → F` is not simple.

Graph is **connected** if there is a path between any two nodes meaning that you should be able to reach another node by starting from any other node. 

**Components** are each separate part of a graph. In below graph `{1, 2, 3, 4}` and `{5}` are the components of the graph.

![Disconnected Graph](http://1.bp.blogspot.com/-5qqeNCOEwIU/UO_tOGNPEAI/AAAAAAAAAks/YWql0-VRFNI/s1600/disconnected+graph.jpg) 

**Tree** is a *connected* graph with *n-1* nodes so there is one and only one *unique* path between any two nodes. If we take `{1, 2, 3, 4}` component of above graph as a separate graph, it would be a tree.

**Weighted graph** is a graph which has weight to every edge. Topmost Image is a weighted graph whereas above image is not. These weights can be imagined as lengths of the edges.

**Neighbor nodes or adjacent nodes** are nodes which have one edge between them. In first image `B, H and F` are neighbors of `A`. 

**Degree** of a node is number of neighbors it has (or number of edges it has). So degree of `A` is 3. *Sum of degrees of a graph is `2m` where `m` is number of edges.* **Indegree** is number of incoming edges a node has. Similarly **outdegree** is number of outgoing edges. **Regular graph** is a graph in which all nodes have same degree. **Complete graph** is a graph which has `n-1` edges (meaning all nodes are connected to each other).

**Coloring** a graph means giving nodes colors so that no neighbor nodes have the same color. **Bipartite graph** is a graph which can be colored by using 2 colors. *A graph is not bipartite if and only if it contains a cycle with odd number of nodes.*

**Simple graph** is a graph which does not have edges that start and end at the same node and does not have multiple edges between two nodes.



## Graph Representation

### Unweighted Graphs

![Unweighted Graph](http://www.algolist.net/img/graphs/graph-ir-1.png) 

```python
# Adjacency List Representation
# Each node contains its neighbor nodes
adjLstGraph = {
    1: {4},
    2: {4, 5},
    3: {5},
    4: {3, 5},
    5: {2, 3, 4}
}

# Adjacency Matrix Representation
# Each row and column represent a node and 
# values represent 1 if there is an edge, 0 if no edge
adjMatGraph = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
]

# Edge List Representation
# Each tuple represent a node between two nodes
# use if finding edges that start at a node is not important
edgeLstGraph = {
    (1, 4),
    (2, 4),
    (5, 4),
    (2, 5),
    (3, 5),
}
```

### Weighted Graphs

![Weighted Graph](https://www.geeksforgeeks.org/wp-content/uploads/graph-STL.png) 

```python
# Adjacency List Representation
# Each node contains its neighbor nodes and its weight
adjLstGraph = {
    0: {1:10, 2:3, 3:2},
    1: {3:7},
    2: {3:6},
    3: {},
}

# Adjacency Matrix Representation
# Values represent weights, 0 if no edge
adjMatGraph = [
    [0, 10, 3, 2],
    [0, 0, 7, 0],
    [0, 0, 0, 6],
    [0, 0, 0, 0],
]

# Edge List Representation
# Each tuple represent a node between two nodes and weight (a, b, w)
edgeLstGraph = {
    (0, 1, 10),
    (0, 2, 3),
    (0, 3, 2),
    (1, 3, 7),
    (2, 3, 6),
}
```

