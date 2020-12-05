import time

import pydot


def plot_recursion_tree(func):
    recursion_tree, counter = None, None

    def init_recursion_tree():
        nonlocal recursion_tree, counter
        counter = 0
        recursion_tree = pydot.Dot(graph_type="digraph")

    def create_node_label(*args):
        nonlocal counter
        return f"{', '.join(map(str, args))} [{counter}]"

    def update_recursion_tree(*args, **kwargs):
        nonlocal recursion_tree, counter
        counter += 1
        curr_node_label = create_node_label(*args)
        recursion_tree.add_node(pydot.Node(curr_node_label, style='filled'))
        if prev_node_label := kwargs.get('node_label'):
            recursion_tree.add_edge(pydot.Edge(prev_node_label, curr_node_label))
        return curr_node_label

    def display_recursion_tree():
        nonlocal recursion_tree
        recursion_tree.write_png(f"plots/{func.__name__}_{int(time.time())}.png")

    def wrapper(*args, **kwargs):
        root = 'node_label' not in kwargs
        if root:
            init_recursion_tree()

        node_label = update_recursion_tree(*args, **kwargs)
        result = func(*args, **{**kwargs, 'node_label': node_label})

        if root:
            display_recursion_tree()
        return result

    return wrapper
