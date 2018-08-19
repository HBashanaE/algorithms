class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None


def pre_order(tree: Node) -> list:
    pre_order_list = []
    stack = [tree]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        pre_order_list.append(node.data)
        stack.append(node.right)
        stack.append(node.left)
    return pre_order_list


def in_order(tree: Node) -> list:
    in_order_list = []
    stack = [tree]
    nodes_analyzed = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node in nodes_analyzed:
            in_order_list.append(node.data)
            continue
        nodes_analyzed.add(node)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)
    return in_order_list


def post_order(tree: Node) -> list:
    post_order_list = []
    stack = [tree]
    nodes_analyzed = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node in nodes_analyzed:
            post_order_list.append(node.data)
            continue
        nodes_analyzed.add(node)
        stack.append(node)
        stack.append(node.right)
        stack.append(node.left)
    return post_order_list
