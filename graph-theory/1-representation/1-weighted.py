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


