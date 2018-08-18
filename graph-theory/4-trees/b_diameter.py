def diameter_dp(tree: dict, nodes: int, root: int=0) -> int:
    """Find diameter of a tree using dynamic programming
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    to_leaf = [0]*nodes
    max_length = [0]*nodes
    _recurse(tree, nodes, root, -1, to_leaf, max_length)
    return max(max_length)


def diameter(tree: dict, start: int=0) -> int:
    """Find diameter using 2 DFSs
    Suitable for event large trees
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""
    node_x = start
    node_y, _ = _dfs(tree, node_x)
    _, max_diameter = _dfs(tree, node_y)
    return max_diameter


def _recurse(tree: dict, nodes: int, current: int, parent: int, to_leaf: list, max_length: list) -> None:
    """Find diameter of a tree using dynamic programming(Helper function)
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    # Many children, so 2 max lengths exists
    max_a = -1
    max_b = -1
    # For each child
    for child in tree[current]:
        if child == parent:
            # This 'child' is actually parent, so pass
            continue
        # Recursively find in the child sub tree
        _recurse(tree, nodes, child, current,
                 to_leaf, max_length)
        # Find biggest and second biggest
        if max_a < to_leaf[child]:
            max_a = to_leaf[child]
        elif max_b < to_leaf[child]:
            max_b = to_leaf[child]
    # Length to leaf is length of the child to its leaf + 1(edge between child and current)
    # Diameter of the current sub tree is lengths of two max lengths to leaves  + 2
    # 2 because we have to consider edges between those 2 children to current
    if max_a == -1:
        # No children
        to_leaf[current] = 0
        max_length[current] = 0
    elif max_b == -1:
        # One child
        to_leaf[current] = max_a + 1
        max_length[current] = max_a + 1
    else:
        # Multiple children
        to_leaf[current] = max_a + 1
        max_length[current] = max_a + max_b + 2


def _dfs(tree: dict, start: int):
    """Simple DFS algorithm which when given a starting node 
    gives the node furthest and distance to it
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    stack = [(start, -1, 0)]
    max_dist = 0
    max_dist_node = start
    while stack:
        current, parent, dist = stack.pop()
        if dist > max_dist:
            max_dist = dist
            max_dist_node = current
        for child in tree[current]:
            if child == parent:
                continue
            stack.append((child, current, dist + 1))
    return max_dist_node, max_dist
