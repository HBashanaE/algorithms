"""
Converting from one graph representation to another.
"""
import b_weighted


def adjacency_list_to_adjacency_matrix(adj_list: dict, nodes: int) -> list:
    """Graph should have nodes as 0..n"""

    adj_mat = [[0]*nodes for _ in range(nodes)]
    for node in adj_list:
        for neighbor in adj_list[node]:
            adj_mat[node][neighbor] = adj_list[node][neighbor]

    return adj_mat


def adjacency_list_to_edge_list(adj_list: dict, nodes: int) -> set:
    """Edge List Items will be sorted so node with smaller index will appear first"""

    edge_list = set()
    for node in adj_list:
        for neighbor in adj_list[node]:
            edge = (node, neighbor, adj_list[node][neighbor])
            edge_list.add(edge)
    return edge_list


def adjacency_matrix_to_adjacency_list(adj_mat: list, nodes: int) -> dict:
    """Adjacency List will have indexed nodes 0...n"""

    adj_list = {}
    for node in range(nodes):
        adj_list[node] = {}
        for neighbor in range(nodes):
            if adj_mat[node][neighbor] != 0:
                adj_list[node][neighbor] = adj_mat[node][neighbor]
    return adj_list


def adjacency_matrix_to_edge_list(adj_mat: list, nodes: int) -> set:
    """Edge List will have indexed nodes 0...n"""

    edge_list = set()
    for node in range(nodes):
        for neighbor in range(nodes):
            if adj_mat[node][neighbor] != 0:
                edge_list.add((node, neighbor, adj_mat[node][neighbor]))
    return edge_list


def edge_list_to_adjacency_list(edge_lst: set, nodes: int) -> dict:
    """Graph should have nodes as 0..n"""

    adj_list = {node: {} for node in range(nodes)}
    for edge in edge_lst:
        a, b, w = edge
        adj_list[a][b] = w
    return adj_list


def edge_list_to_adjacency_matrix(edge_lst: set, nodes: int) -> list:
    """Graph should have nodes as 0..n"""

    adj_mat = [[0]*nodes for _ in range(nodes)]
    for edge in edge_lst:
        a, b, w = edge
        adj_mat[a][b] = w
    return adj_mat
