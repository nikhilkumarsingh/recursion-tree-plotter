import os
import time
from itertools import count

import pydot


class _RecursionTreePlotter:
    def __init__(self, func_name):
        self._func_name = func_name
        self._plot = pydot.Dot(graph_type='digraph')
        self._call_count = count(1)
        self._stack = []

    def enter(self, *args, **kwargs):
        self._stack.append(self._create_node_label(*args, **kwargs))

        self._plot.add_node(pydot.Node(self._stack[-1], style='filled'))
        if len(self._stack) > 1:
            self._plot.add_edge(pydot.Edge(self._stack[-2], self._stack[-1]))

    def exit(self):
        self._stack.pop()

        if not self._stack:
            self._save_image()

    def _create_node_label(self, *args, **kwargs):
        arg_string = ', '.join([str(arg) for arg in args] + [f'{k}={v}' for k, v in kwargs.items()])
        return f'{arg_string} [{next(self._call_count)}]'

    def _save_image(self):
        self._plot.write_png(os.path.join(os.getcwd(), f'{self._func_name}_{int(time.time())}.png'))


def plot_recursion_tree(func):
    plotter = _RecursionTreePlotter(func_name=func.__name__)

    def wrapper(*args, **kwargs):
        plotter.enter(*args, **kwargs)
        result = func(*args, **kwargs)
        plotter.exit()

        return result

    return wrapper
