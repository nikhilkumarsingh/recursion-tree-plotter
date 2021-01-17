import sys

sys.path.append('../')
from recursion_tree_plotter.recursion_tree_plotter import plot_recursion_tree


@plot_recursion_tree
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(5)
