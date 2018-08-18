import unittest
import a_tree_traversal
import b_diameter

tree = {
    0: {1, 2},
    1: {0, 3, 4, 5},
    2: {0, 6},
    3: {1, 7},
    4: {1, 8, 9},
    5: {1},
    6: {2},
    7: {3},
    8: {4},
    9: {4},
}
nodes = 10


class TestTreeTraversal(unittest.TestCase):
    def test_dfs_tree(self):
        self.assertEqual(
            a_tree_traversal.dfs_tree(tree, 0, -1),
            nodes
        )

    def test_dfs_tree_iter(self):
        self.assertEqual(
            a_tree_traversal.dfs_tree_iter(tree, 0),
            nodes
        )

    def test_bfs_tree_iter(self):
        self.assertEqual(
            a_tree_traversal.bfs_tree_iter(tree, 0),
            nodes
        )

    def test_count_sub_tree_node(self):
        self.assertListEqual(
            a_tree_traversal.count_nodes(tree, 0, -1, [0]*nodes),
            [10, 7, 2, 2, 3, 1, 1, 1, 1, 1]
        )


class TestDiameter(unittest.TestCase):
    def test_diameter_dp(self):
        for start in range(10):
            self.assertEqual(
                b_diameter.diameter_dp(tree, nodes, start),
                5
            )

    def test_diameter(self):
        for start in range(10):
            self.assertEqual(
                b_diameter.diameter(tree, start),
                5
            )


if __name__ == '__main__':
    unittest.main()
