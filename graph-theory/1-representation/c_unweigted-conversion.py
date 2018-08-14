"""
Converting from one graph representation to another.
"""
import a_unweighted


def adjacencyListToAdjacencyMatrix(adjList: dict) -> list:
    """Graph should have nodes as 0..n"""

    n = len(adjList)
    adjMat = [[0]*n for _ in range(n)]
    for node in adjList:
        for neighbor in adjList[node]:
            adjMat[node][neighbor] = 1

    return adjMat


def adjacencyListToEdgeList(adjList: dict) -> set:
    """Edge List Items will be sorted so node with smaller index will appear first"""

    edgeList = set()
    for node in adjList:
        for neighbor in adjList[node]:
            edge = (node, neighbor)
            edgeList.add(edge)
    return edgeList


def adjacencyMatrixToAdjacencyList(adjMat: list) -> dict:
    """Adjacency List will have indexed nodes 0...n"""

    adjList = {}
    n = len(adjMat)
    for node in range(n):
        adjList[node] = set()
        for neighbor in range(n):
            if adjMat[node][neighbor] == 1:
                adjList[node].add(neighbor)
    return adjList


def adjacencyMatrixToEdgeList(adjMat: list) -> set:
    """Edge List will have indexed nodes 0...n"""

    edgeList = set()
    n = len(adjMat)
    for node in range(n):
        for neighbor in range(n):
            if adjMat[node][neighbor] == 1:
                edgeList.add((node, neighbor))
    return edgeList


def edgeListToAdjacencyList(edgeLst: set) -> dict:
    """Graph should have nodes as 0..n"""

    adjLst = {}
    for edge in edgeLst:
        a, b = edge
        if a not in adjLst:
            adjLst[a] = set()
        if b not in adjLst:
            adjLst[b] = set()
        adjLst[a].add(b)
    max_node = max(adjLst)
    for node in range(max_node + 1):
        if node not in adjLst:
            adjLst[node] = set()
    return adjLst


def edgeListToAdjacencyMatrix(edgeLst: set) -> list:
    """Graph should have nodes as 0..n"""

    max_node = -1
    for edge in edgeLst:
        bigger_node = max(edge)
        max_node = max(max_node, bigger_node)
    n = max_node + 1
    adjMat = [[0]*n for _ in range(n)]
    for edge in edgeLst:
        a, b = edge
        adjMat[a][b] = 1
    return adjMat


# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
assert(
    adjacencyListToAdjacencyMatrix(a_unweighted.adjLstGraph)
    ==
    a_unweighted.adjMatGraph
)
assert(
    adjacencyListToEdgeList(a_unweighted.adjLstGraph)
    ==
    a_unweighted.edgeLstGraph
)
assert(
    adjacencyMatrixToAdjacencyList(a_unweighted.adjMatGraph)
    ==
    a_unweighted.adjLstGraph
)
assert(
    adjacencyMatrixToEdgeList(a_unweighted.adjMatGraph)
    ==
    a_unweighted.edgeLstGraph
)
assert(
    edgeListToAdjacencyList(a_unweighted.edgeLstGraph)
    ==
    a_unweighted.adjLstGraph
)
assert(
    edgeListToAdjacencyMatrix(a_unweighted.edgeLstGraph)
    ==
    a_unweighted.adjMatGraph
)
