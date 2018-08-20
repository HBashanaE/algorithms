import unittest

import a_dfs
import b_bfs
import c_usage_connectivity
import d_usage_cycles
import e_usage_coloring

graph_a = {
    0: {1, 2, 4},
    1: {0, 2, 3, 4},
    2: {0, 1},
    3: {1},
    4: {0, 1},
    5: set()
}
graph_b = {
    1: {2, 5},
    2: {1, 5, 3},
    3: {2, 4},
    4: {3, 5, 6},
    5: {1, 2, 4},
    6: {4}
}
nodes_b = 6
graph_c = {
    1: {4},
    2: {4},
    3: {4},
    4: {1, 2, 3, 5},
    5: {4, 6},
    6: {5},
}
nodes_c = 6


class TestDFS(unittest.TestCase):
    def test_dfs_recursion(self):
        self.assertEqual(a_dfs.dfs_recursion(graph_a, 0, set()), {0, 1, 2, 3, 4})

    def test_dfs_iter(self):
        self.assertEqual(a_dfs.dfs_iter(graph_a, 0), {0, 1, 2, 3, 4})


class TestBFS(unittest.TestCase):
    def test_bfs_iter(self):
        self.assertEqual(b_bfs.bfs_iter(graph_a, 0), {0, 1, 2, 3, 4})

    def test_bfs_distance(self):
        self.assertEqual(b_bfs.bfs_distance(graph_a, 0, 3), 2)


class TestConnectivity(unittest.TestCase):
    def test_is_connected(self):
        self.assertFalse(c_usage_connectivity.is_connected(graph_a))

    def test_list_components(self):
        self.assertListEqual(c_usage_connectivity.list_components(graph_a), [{0, 1, 2, 3, 4}, {5}])


class TestCycle(unittest.TestCase):
    def test_contains_cycle(self):
        self.assertTrue(d_usage_cycles.contains_cycle(graph_b))
        self.assertFalse(d_usage_cycles.contains_cycle(graph_c))

    def test_contains_cycle_specific(self):
        self.assertTrue(d_usage_cycles.contains_cycle_specific(graph_b, nodes_b))
        self.assertFalse(d_usage_cycles.contains_cycle_specific(graph_c, nodes_c))


class TestBipartite(unittest.TestCase):
    def test_is_bipartite(self):
        self.assertFalse(e_usage_coloring.is_bipartite(graph_b))
        self.assertTrue(e_usage_coloring.is_bipartite(graph_c))


if __name__ == '__main__':
    unittest.main()
