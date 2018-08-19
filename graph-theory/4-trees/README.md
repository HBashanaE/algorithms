# Tree Algorithms

## Tree Traversal

Depth First Search implementation using recursion and iteration. Depth First Search implementation using  iteration. Dynamic Programming example demonstrated by using recursive solution to count all sub tree nodes starting from a node. Tested on below tree.

![Traversal](../README/tree-3.jpeg)

**File: `a_tree_traversal.py`**

## Diameter

Finding diameter of a tree using Algorithm A and algorithm B. Algorithm A in implemented recursively. Algorithm B is implemented iteratively. Tested on above tree.

**File: `b_diameter.py`**

## All Longest Paths

All longest paths starting from each node. Algorithm A in implemented recursively. Trivial to convert to iterative function. Tested on above tree.

**File: `c_longest_paths.py`**

### Binary Trees

![Binary Tree](../README/tree-5.png)

Binary Tree simple implementation. Pre-order, in-order and post-order algorithms implemented. Tested on above tree.

**File: `d_binary_tree.py`**

## Time Complexities

| Algorithm             | Description                                                  | Time Complexity |
| --------------------- | ------------------------------------------------------------ | --------------- |
| `dfs_tree()`          | DFS recursive algorithm. Not suitable for large trees.       | `O(n)`          |
| `dfs_tree_iter()`     | DFS iterative algorithm.                                     | `O(n)`          |
| `bfs_tree_iter()`     | BFS iterative algorithm.                                     | `O(n)`          |
| `count_nodes()`       | Counts nodes in each sub-tree. Demonstrates dynamic-programming. | `O(n)`          |
| `diameter_dp()`       | Finds diameter using recursive method. Can be converted to an iterative method easily. Uses dynamic programming. | `O(n)`          |
| `diameter()`          | Find diameter using two DFS traversals.                      | `O(n)`          |
| `all_longest_paths()` | Gets lengths of all longest paths starting from a node using recursive method. Can be converted to an iterative method easily. Uses dynamic programming. | `O(n)`          |

`n` = no of nodes