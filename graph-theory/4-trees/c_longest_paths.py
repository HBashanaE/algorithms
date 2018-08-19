def all_longest_paths(tree: dict, nodes: int, root: int):
    max_len_child_1 = [(0, -1)] * nodes
    max_len_child_2 = [(0, -1)] * nodes
    # get maximum lengths through children
    _max_length_through_child(tree, max_len_child_1, max_len_child_2, root, -1)
    max_length = [(0, -1)] * nodes
    # get maximum lengths
    _max_length(tree, max_length, max_len_child_1, max_len_child_2, root, -1)
    max_lengths_only = [max_length[i][0] for i in range(nodes)]
    return max_lengths_only


def _max_length_through_child(tree: dict, max_len_child_1: list, max_len_child_2: list, node: int, parent: int):
    """Gets maximum length which starts from each node and goes down the rooted tree
    This stores maximum and second maximum numbers and child from which the path started
    in  a tuple as in (DISTANCE, PATH_STARTING_CHILD)
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""
    # First is the length and second is the child node it goes through
    max_len_child_1_of_current = (-1, -1)
    max_len_child_2_of_current = (-1, -1)
    for child in tree[node]:
        if child == parent:
            continue
        # recurse to child nodes
        _max_length_through_child(tree, max_len_child_1, max_len_child_2, child, node)
        # record best and second best
        if max_len_child_1_of_current[0] < max_len_child_1[child][0]:
            max_len_child_1_of_current = (max_len_child_1[child][0] + 1, child)
        elif max_len_child_2_of_current[0] < max_len_child_1[child][0]:
            max_len_child_2_of_current = (max_len_child_1[child][0] + 1, child)
    if max_len_child_1_of_current[0] == -1 and max_len_child_2_of_current[0] == -1:
        # No child
        max_len_child_1[node] = (0, -1)
        max_len_child_2[node] = (0, -1)
    elif max_len_child_2_of_current[0] == -1:
        # One child
        max_len_child_1[node] = max_len_child_1_of_current
        max_len_child_2[node] = (0, -1)
    else:
        # Multiple children
        max_len_child_1[node] = max_len_child_1_of_current
        max_len_child_2[node] = max_len_child_2_of_current


def _max_length(tree: dict, max_length: list, max_len_child_1: list, max_len_child_2: list, node: int, parent: int):
    """Gets maximum length which starts from each node
    Uses tuples as in (DISTANCE, PATH_STARTING_CHILD)
    Tree has to be passed as an adjacency list.
    Nodes has to be indexed 0..n."""
    if parent == -1:
        # No parent
        max_len_parent = (0, -1)
    elif max_length[parent][1] != node:
        # Max length through parent doesn't goes through the node
        max_len_parent = (max_length[parent][0] + 1, parent)
    elif max_len_child_1[parent][1] != node:
        # Max length through parent goes through the node
        max_len_parent = (max_len_child_1[parent][0] + 1, parent)
    else:
        # Max length through parent goes through the node
        max_len_parent = (max_len_child_2[parent][0] + 1, parent)
    # get maximum length accessible through its children
    max_len_child = max_len_child_1[node]
    if max_len_child > max_len_parent:
        max_length[node] = max_len_child
    else:
        max_length[node] = max_len_parent

    # recurse for children
    for child in tree[node]:
        if child == parent:
            continue
        _max_length(tree, max_length, max_len_child_1, max_len_child_2, child, node)
