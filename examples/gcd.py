import sys

sys.path.append('../')
from recursion_tree_plotter import plot_recursion_tree


@plot_recursion_tree
def gcd(a, b, **kwargs):
    if b == 0:
        return a
    return gcd(b, a % b, **kwargs)


if __name__ == "__main__":
    gcd(24, 30)
