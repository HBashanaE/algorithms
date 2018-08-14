"""
Converting from one graph representation to another.
"""
import b_weighted


def adjacency_list_to_adjacency_matrix(adj_list: dict) -> list:
    """Graph should have nodes as 0..n"""

    n = len(adj_list)
    adj_mat = [[0]*n for _ in range(n)]
    for node in adj_list:
        for neighbor in adj_list[node]:
            adj_mat[node][neighbor] = adj_list[node][neighbor]

    return adj_mat


def adjacency_list_to_edge_list(adj_list: dict) -> set:
    """Edge List Items will be sorted so node with smaller index will appear first"""

    edge_list = set()
    for node in adj_list:
        for neighbor in adj_list[node]:
            edge = (node, neighbor, adj_list[node][neighbor])
            edge_list.add(edge)
    return edge_list


def adjacency_matrix_to_adjacency_list(adj_mat: list) -> dict:
    """Adjacency List will have indexed nodes 0...n"""

    adj_list = {}
    n = len(adj_mat)
    for node in range(n):
        adj_list[node] = {}
        for neighbor in range(n):
            if adj_mat[node][neighbor] != 0:
                adj_list[node][neighbor] = adj_mat[node][neighbor]
    return adj_list


def adjacency_matrix_to_edge_list(adj_mat: list) -> set:
    """Edge List will have indexed nodes 0...n"""

    edge_list = set()
    n = len(adj_mat)
    for node in range(n):
        for neighbor in range(node, n):
            if adj_mat[node][neighbor] != 0:
                edge_list.add((node, neighbor, adj_mat[node][neighbor]))
    return edge_list


def edge_list_to_adjacency_list(edge_lst: set) -> dict:
    """Graph should have nodes as 0..n"""

    adj_lst = {}
    for edge in edge_lst:
        a, b, w = edge
        if a not in adj_lst:
            adj_lst[a] = {}
        if b not in adj_lst:
            adj_lst[b] = {}
        adj_lst[a][b] = w
    max_node = max(adj_lst)
    for node in range(max_node + 1):
        if node not in adj_lst:
            adj_lst[node] = {}
    return adj_lst


def edge_list_to_adjacency_matrix(edge_lst: set) -> list:
    """Graph should have nodes as 0..n"""

    max_node = -1
    for edge in edge_lst:
        bigger_node = max(edge[0], edge[1])
        max_node = max(max_node, bigger_node)
    n = max_node + 1
    adj_mat = [[0]*n for _ in range(n)]
    for edge in edge_lst:
        a, b, w = edge
        if b < a:
            a, b = b, a
        adj_mat[a][b] = w
    return adj_mat


# -----------------------------------------------------------------------
# TESTS -----------------------------------------------------------------
# -----------------------------------------------------------------------
assert(
    adjacency_list_to_adjacency_matrix(b_weighted.adj_list_graph)
    ==
    b_weighted.adj_matrix_graph
)
assert(
    adjacency_list_to_edge_list(b_weighted.adj_list_graph)
    ==
    b_weighted.edge_list_graph
)
assert(
    adjacency_matrix_to_adjacency_list(b_weighted.adj_matrix_graph)
    ==
    b_weighted.adj_list_graph
)
assert(
    adjacency_matrix_to_edge_list(b_weighted.adj_matrix_graph)
    ==
    b_weighted.edge_list_graph
)
assert(
    edge_list_to_adjacency_list(b_weighted.edge_list_graph)
    ==
    b_weighted.adj_list_graph
)
assert(
    edge_list_to_adjacency_matrix(b_weighted.edge_list_graph)
    ==
    b_weighted.adj_matrix_graph
)
