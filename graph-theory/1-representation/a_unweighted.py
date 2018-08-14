"""
Adjacency List Representation.
Each node contains its neighbor nodes.
"""
adjLstGraph = {
    0: set(),
    1: {4},
    2: {4, 5},
    3: {5},
    4: {1, 2, 5},
    5: {2, 3, 4}
}

"""
Adjacency Matrix Representation.
Each row and column represent a node and values represent 1 if there is an edge, 0 if no edge.
"""
adjMatGraph = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 0],
]

"""
Edge List Representation.
Each tuple represent a node between two nodes use if finding edges that start at a node is not important.
"""
edgeLstGraph = {
    (1, 4),
    (2, 4),
    (4, 1),
    (4, 2),
    (4, 5),
    (2, 5),
    (3, 5),
    (5, 2),
    (5, 3),
    (5, 4),
}
