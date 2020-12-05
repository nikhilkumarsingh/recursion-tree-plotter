import sys

sys.path.append('../')
from recursion_tree_plotter import plot_recursion_tree


@plot_recursion_tree
def fib(n, **kwargs):
    if n <= 1:
        return n
    return fib(n - 1, **kwargs) + fib(n - 2, **kwargs)


if __name__ == "__main__":
    fib(5)
