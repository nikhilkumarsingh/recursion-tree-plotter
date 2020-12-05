import sys

sys.path.append('../')
from recursion_tree_plotter import plot_recursion_tree


@plot_recursion_tree
def fac(n, **kwargs):
    if n <= 1:
        return 1
    return n * fac(n - 1, **kwargs)


if __name__ == "__main__":
    fac(10)
