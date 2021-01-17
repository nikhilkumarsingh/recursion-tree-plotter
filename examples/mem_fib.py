import sys

sys.path.append('../')
from recursion_tree_plotter.recursion_tree_plotter import plot_recursion_tree


@plot_recursion_tree
def mem_fib(n, **kwargs):
    if n <= 1:
        return n
    if n in kwargs['mem']:
        return kwargs['mem'][n]

    kwargs['mem'][n] = mem_fib(n - 1, **kwargs) + mem_fib(n - 2, **kwargs)
    return kwargs['mem'][n]


if __name__ == "__main__":
    mem_fib(10, mem={})
