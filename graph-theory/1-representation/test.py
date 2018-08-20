import unittest

from a_unweighted import *
from b_weighted import *
from c_unweigted_conversion import *
from d_weigted_conversion import *


class TestUnweightedConversion(unittest.TestCase):
    def test_adjacency_list_to_adjacency_matrix(self):
        self.assertEqual(adjacency_list_to_adjacency_matrix_unweighted(adj_list_graph, nodes), adj_matrix_graph)

    def test_adjacency_list_to_edge_list(self):
        self.assertEqual(adjacency_list_to_edge_list_unweighted(adj_list_graph), edge_list_graph)

    def test_adjacency_matrix_to_adjacency_list(self):
        self.assertEqual(adjacency_matrix_to_adjacency_list_unweighted(adj_matrix_graph, nodes), adj_list_graph)

    def test_adjacency_matrix_to_edge_list(self):
        self.assertEqual(
            adjacency_matrix_to_edge_list_unweighted(adj_matrix_graph, nodes), edge_list_graph)

    def test_edge_list_to_adjacency_list(self):
        self.assertEqual(edge_list_to_adjacency_list_unweighted(edge_list_graph, nodes), adj_list_graph)

    def test_edge_list_to_adjacency_matrix(self):
        self.assertEqual(edge_list_to_adjacency_matrix_unweighted(edge_list_graph, nodes), adj_matrix_graph)


class TestWeightedConversion(unittest.TestCase):
    def test_adjacency_list_to_adjacency_matrix(self):
        self.assertEqual(adjacency_list_to_adjacency_matrix_weighted(adj_list_graph, nodes), adj_matrix_graph)

    def test_adjacency_list_to_edge_list(self):
        self.assertEqual(adjacency_list_to_edge_list_weighted(adj_list_graph, nodes), edge_list_graph)

    def test_adjacency_matrix_to_adjacency_list(self):
        self.assertEqual(adjacency_matrix_to_adjacency_list_weighted(adj_matrix_graph, nodes), adj_list_graph)

    def test_adjacency_matrix_to_edge_list(self):
        self.assertEqual(adjacency_matrix_to_edge_list_weighted(adj_matrix_graph, nodes), edge_list_graph)

    def test_edge_list_to_adjacency_list(self):
        self.assertEqual(edge_list_to_adjacency_list_weighted(edge_list_graph, nodes), adj_list_graph)

    def test_edge_list_to_adjacency_matrix(self):
        self.assertEqual(edge_list_to_adjacency_matrix_weighted(edge_list_graph, nodes), adj_matrix_graph)


if __name__ == '__main__':
    unittest.main()
