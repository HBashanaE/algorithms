import unittest

import a_tree_traversal
import b_diameter
import c_longest_paths
import d_binary_tree

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
            a_tree_traversal.count_nodes(tree, 0, -1, [0] * nodes),
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


class TestAllLongestPaths(unittest.TestCase):
    def test_all_longest_paths(self):
        self.assertListEqual(
            c_longest_paths.all_longest_paths(tree, nodes, 0),
            [3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
        )


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        binary_tree = d_binary_tree.Node(2)
        binary_tree.right = d_binary_tree.Node(5)
        binary_tree.right.right = d_binary_tree.Node(9)
        binary_tree.right.right.left = d_binary_tree.Node(4)
        binary_tree.left = d_binary_tree.Node(7)
        binary_tree.left.right = d_binary_tree.Node(6)
        binary_tree.left.right.right = d_binary_tree.Node(11)
        binary_tree.left.right.left = d_binary_tree.Node(5)
        binary_tree.left.left = d_binary_tree.Node(2)
        self.binary_tree = binary_tree

    def test_pre_order(self):
        self.assertListEqual(
            d_binary_tree.pre_order(self.binary_tree),
            [2, 7, 2, 6, 5, 11, 5, 9, 4]
        )

    def test_in_order(self):
        self.assertListEqual(
            d_binary_tree.in_order(self.binary_tree),
            [2, 7, 5, 6, 11, 2, 5, 4, 9]
        )

    def test_post_order(self):
        self.assertListEqual(
            d_binary_tree.post_order(self.binary_tree),
            [2, 5, 11, 6, 7, 4, 9, 5, 2]
        )


if __name__ == '__main__':
    unittest.main()
