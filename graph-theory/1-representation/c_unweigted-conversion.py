"""
Converting from one graph representation to another.
"""
import a_unweighted


def adjacency_list_to_adjacency_matrix(adj_list: dict) -> list:
    """Graph should have nodes as 0..n"""

    n = len(adj_list)
    adj_mat = [[0]*n for _ in range(n)]
    for node in adj_list:
        for neighbor in adj_list[node]:
            adj_mat[node][neighbor] = 1

    return adj_mat


def adjacency_list_to_edge_list(adj_list: dict) -> set:
    """Edge List Items will be sorted so node with smaller index will appear first"""

    edge_list = set()
    for node in adj_list:
        for neighbor in adj_list[node]:
            edge = (node, neighbor)
            edge_list.add(edge)
    return edge_list


def adjacency_matrix_to_adjacency_list(adj_mat: list) -> dict:
    """Adjacency List will have indexed nodes 0...n"""

    adj_list = {}
    n = len(adj_mat)
    for node in range(n):
        adj_list[node] = set()
        for neighbor in range(n):
            if adj_mat[node][neighbor] == 1:
                adj_list[node].add(neighbor)
    return adj_list


def adjacency_matrix_to_edge_list(adj_mat: list) -> set:
    """Edge List will have indexed nodes 0...n"""

    edge_list = set()
    n = len(adj_mat)
    for node in range(n):
        for neighbor in range(n):
            if adj_mat[node][neighbor] == 1:
                edge_list.add((node, neighbor))
    return edge_list


def edge_list_to_adjacency_list(edge_list: set) -> dict:
    """Graph should have nodes as 0..n"""

    adj_list = {}
    for edge in edge_list:
        a, b = edge
        if a not in adj_list:
            adj_list[a] = set()
        if b not in adj_list:
            adj_list[b] = set()
        adj_list[a].add(b)
    max_node = max(adj_list)
    for node in range(max_node + 1):
        if node not in adj_list:
            adj_list[node] = set()
    return adj_list


def edge_list_to_adjacency_matrix(edge_list: set) -> list:
    """Graph should have nodes as 0..n"""

    max_node = -1
    for edge in edge_list:
        bigger_node = max(edge)
        max_node = max(max_node, bigger_node)
    n = max_node + 1
    adj_mat = [[0]*n for _ in range(n)]
    for edge in edge_list:
        a, b = edge
        adj_mat[a][b] = 1
    return adj_mat


# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
assert(
    adjacency_list_to_adjacency_matrix(a_unweighted.adj_list_graph)
    == a_unweighted.adj_matrix_graph
)
assert(
    adjacency_list_to_edge_list(a_unweighted.adj_list_graph)
    == a_unweighted.edge_list_graph
)
assert(
    adjacency_matrix_to_adjacency_list(a_unweighted.adj_matrix_graph)
    == a_unweighted.adj_list_graph
)
assert(
    adjacency_matrix_to_edge_list(a_unweighted.adj_matrix_graph)
    == a_unweighted.edge_list_graph
)
assert(
    edge_list_to_adjacency_list(a_unweighted.edge_list_graph)
    == a_unweighted.adj_list_graph
)
assert(
    edge_list_to_adjacency_matrix(a_unweighted.edge_list_graph)
    == a_unweighted.adj_matrix_graph
)
