import collections


def dfs_tree(tree: dict, current: int, parent: int) -> int:
    """DFS to traverse a tree. Not good for large Trees.
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    sub_tree_nodes = 1
    for child in tree[current]:
        if parent == child:
            continue
        sub_tree_nodes += dfs_tree(tree, current=child, parent=current)
    return sub_tree_nodes


def dfs_tree_iter(tree: dict, start: int) -> int:
    """DFS to traverse a tree. Better for large Trees.
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    nodes = 0
    stack = [(start, -1)]
    while stack:
        current, parent = stack.pop()
        nodes += 1
        for child in tree[current]:
            if child == parent:
                continue
            stack.append((child, current))
    return nodes


def bfs_tree_iter(tree: dict, start: int) -> int:
    """BFS to traverse a tree
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    nodes = 0
    queue = collections.deque([(start, -1)])
    while queue:
        current, parent = queue.pop()
        nodes += 1
        for child in tree[current]:
            if child == parent:
                continue
            queue.appendleft((child, current))
    return nodes


def count_nodes(tree: dict, current: int, parent: int, nodes: list) -> list:
    """DFS to count no of nodes in each sub tree
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""

    nodes[current] = 1
    for child in tree[current]:
        if parent == child:
            continue 
        count_nodes(tree, current=child, parent=current, nodes=nodes)
        nodes[current] += nodes[child]
    return nodes
