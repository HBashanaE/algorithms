"""
Converting from one graph representation to another.
"""
import b_weighted


def adjacencyListToAdjacencyMatrix(adjList: dict) -> list:
    """Graph should have nodes as 0..n"""

    n = len(adjList)
    adjMat = [[0]*n for _ in range(n)]
    for node in adjList:
        for neighbor in adjList[node]:
            adjMat[node][neighbor] = adjList[node][neighbor]

    return adjMat


def adjacencyListToEdgeList(adjList: dict) -> set:
    """Edge List Items will be sorted so node with smaller index will appear first"""

    edgeList = set()
    for node in adjList:
        for neighbor in adjList[node]:
            edge = (node, neighbor, adjList[node][neighbor])
            edgeList.add(edge)
    return edgeList


def adjacencyMatrixToAdjacencyList(adjMat: list) -> dict:
    """Adjacency List will have indexed nodes 0...n"""

    adjList = {}
    n = len(adjMat)
    for node in range(n):
        adjList[node] = {}
        for neighbor in range(n):
            if adjMat[node][neighbor] != 0:
                adjList[node][neighbor] = adjMat[node][neighbor]
    return adjList


def adjacencyMatrixToEdgeList(adjMat: list) -> set:
    """Edge List will have indexed nodes 0...n"""

    edgeList = set()
    n = len(adjMat)
    for node in range(n):
        for neighbor in range(node, n):
            if adjMat[node][neighbor] != 0:
                edgeList.add((node, neighbor, adjMat[node][neighbor]))
    return edgeList


def edgeListToAdjacencyList(edgeLst: set) -> dict:
    """Graph should have nodes as 0..n"""

    adjLst = {}
    for edge in edgeLst:
        a, b, w = edge
        if a not in adjLst:
            adjLst[a] = {}
        if b not in adjLst:
            adjLst[b] = {}
        adjLst[a][b] = w
    max_node = max(adjLst)
    for node in range(max_node + 1):
        if node not in adjLst:
            adjLst[node] = {}
    return adjLst


def edgeListToAdjacencyMatrix(edgeLst: set) -> list:
    """Graph should have nodes as 0..n"""

    max_node = -1
    for edge in edgeLst:
        bigger_node = max(edge[0], edge[1])
        max_node = max(max_node, bigger_node)
    n = max_node + 1
    adjMat = [[0]*n for _ in range(n)]
    for edge in edgeLst:
        a, b, w = edge
        if b < a:
            a, b = b, a
        adjMat[a][b] = w
    return adjMat


# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
assert(
    adjacencyListToAdjacencyMatrix(b_weighted.adjLstGraph)
    ==
    b_weighted.adjMatGraph
)
assert(
    adjacencyListToEdgeList(b_weighted.adjLstGraph)
    ==
    b_weighted.edgeLstGraph
)
assert(
    adjacencyMatrixToAdjacencyList(b_weighted.adjMatGraph)
    ==
    b_weighted.adjLstGraph
)
assert(
    adjacencyMatrixToEdgeList(b_weighted.adjMatGraph)
    ==
    b_weighted.edgeLstGraph
)
assert(
    edgeListToAdjacencyList(b_weighted.edgeLstGraph)
    ==
    b_weighted.adjLstGraph
)
assert(
    edgeListToAdjacencyMatrix(b_weighted.edgeLstGraph)
    ==
    b_weighted.adjMatGraph
)
