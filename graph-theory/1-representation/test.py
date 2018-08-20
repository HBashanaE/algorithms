import unittest

import a_unweighted
import b_weighted
import c_unweigted_conversion
import d_weigted_conversion


class TestUnweightedConversion(unittest.TestCase):
    def test_adjacency_list_to_adjacency_matrix(self):
        self.assertEqual(
            c_unweigted_conversion.adjacency_list_to_adjacency_matrix(a_unweighted.adj_list_graph, a_unweighted.nodes),
            a_unweighted.adj_matrix_graph)

    def test_adjacency_list_to_edge_list(self):
        self.assertEqual(c_unweigted_conversion.adjacency_list_to_edge_list(a_unweighted.adj_list_graph),
                         a_unweighted.edge_list_graph)

    def test_adjacency_matrix_to_adjacency_list(self):
        self.assertEqual(c_unweigted_conversion.adjacency_matrix_to_adjacency_list(a_unweighted.adj_matrix_graph,
                                                                                   a_unweighted.nodes),
                         a_unweighted.adj_list_graph)

    def test_adjacency_matrix_to_edge_list(self):
        self.assertEqual(
            c_unweigted_conversion.adjacency_matrix_to_edge_list(a_unweighted.adj_matrix_graph, a_unweighted.nodes),
            a_unweighted.edge_list_graph)

    def test_edge_list_to_adjacency_list(self):
        self.assertEqual(
            c_unweigted_conversion.edge_list_to_adjacency_list(a_unweighted.edge_list_graph, a_unweighted.nodes),
            a_unweighted.adj_list_graph)

    def test_edge_list_to_adjacency_matrix(self):
        self.assertEqual(
            c_unweigted_conversion.edge_list_to_adjacency_matrix(a_unweighted.edge_list_graph, a_unweighted.nodes),
            a_unweighted.adj_matrix_graph)


class TestWeightedConversion(unittest.TestCase):
    def test_adjacency_list_to_adjacency_matrix(self):
        self.assertEqual(
            d_weigted_conversion.adjacency_list_to_adjacency_matrix(b_weighted.adj_list_graph, b_weighted.nodes),
            b_weighted.adj_matrix_graph)

    def test_adjacency_list_to_edge_list(self):
        self.assertEqual(d_weigted_conversion.adjacency_list_to_edge_list(b_weighted.adj_list_graph, b_weighted.nodes),
                         b_weighted.edge_list_graph)

    def test_adjacency_matrix_to_adjacency_list(self):
        self.assertEqual(
            d_weigted_conversion.adjacency_matrix_to_adjacency_list(b_weighted.adj_matrix_graph, b_weighted.nodes),
            b_weighted.adj_list_graph)

    def test_adjacency_matrix_to_edge_list(self):
        self.assertEqual(
            d_weigted_conversion.adjacency_matrix_to_edge_list(b_weighted.adj_matrix_graph, b_weighted.nodes),
            b_weighted.edge_list_graph)

    def test_edge_list_to_adjacency_list(self):
        self.assertEqual(d_weigted_conversion.edge_list_to_adjacency_list(b_weighted.edge_list_graph, b_weighted.nodes),
                         b_weighted.adj_list_graph)

    def test_edge_list_to_adjacency_matrix(self):
        self.assertEqual(
            d_weigted_conversion.edge_list_to_adjacency_matrix(b_weighted.edge_list_graph, b_weighted.nodes),
            b_weighted.adj_matrix_graph)


if __name__ == '__main__':
    unittest.main()
