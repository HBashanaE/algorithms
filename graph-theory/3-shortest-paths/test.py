import unittest

from a_bellman_ford import *
from b_dijkstra import *
from c_floyd_warshall import *

graph_a = {
    (0, 1, 3),
    (0, 3, 5),
    (1, 4, 2),
    (1, 2, 7),
    (2, 5, 9),
    (3, 4, 4),
    (4, 5, 6)
}
nodes_a = 6
graph_b = {
    (0, 1, 5),
    (0, 2, 4),
    (1, 3, 3),
    (2, 1, -6),
    (3, 2, 2)
}
nodes_b = 4
graph_c = {
    0: {3: 5, 1: 3},
    1: {2: 7, 4: 2},
    2: {5: 9},
    3: {4: 4},
    4: {5: 6},
    5: {}
}
nodes_c = 6


class TestBellmanFord(unittest.TestCase):
    def test_bellman_ford(self):
        self.assertListEqual(bellman_ford(graph_a, nodes_a, 0), [0, 3, 10, 5, 5, 11])
        self.assertRaises(TypeError, bellman_ford, graph_b, nodes_b, 0)


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        self.assertListEqual(dijkstra(graph_c, nodes_c, 0), [0, 3, 10, 5, 5, 11])

    def test_dijkstra_heapq(self):
        self.assertListEqual(dijkstra_heapq(graph_c, nodes_c, 0), [0, 3, 10, 5, 5, 11])


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        self.assertListEqual(floyd_warshall(graph_c, nodes_c)[0], [0, 3, 10, 5, 5, 11])


if __name__ == '__main__':
    unittest.main()
