import unittest
import a_bellman_ford

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


class TestCycle(unittest.TestCase):
    def test_contains_cycle_specific(self):
        self.assertListEqual(
            a_bellman_ford.bellman_ford(graph_a, nodes_a, 0),
            [0, 3, 10, 5, 5, 11]
        )
        self.assertRaises(
            TypeError,
            a_bellman_ford.bellman_ford, graph_b, nodes_b, 0
        )


if __name__ == '__main__':
    unittest.main()
