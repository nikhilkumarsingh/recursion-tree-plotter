# Recursion Tree Plotter

A python decorator to generate a visual tree for recursive functions.


## Installation

```bash
$ pip install recursion-tree-plotter
```


## Example

Let's say you have a recursive function for finding n-th element in Fibonacci sequence.

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

In order to plot a recursion tree for an execution of above function (`say fib(5)`), we put `@plot_recursion_tree`
decorator over it.


```python
from recursion_tree_plotter import plot_recursion_tree


@plot_recursion_tree
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

And boom!

![](https://github.com/nikhilkumarsingh/recursion-tree-plotter/raw/master/examples/plots/fib_1607174531.png)


In the tree, node label is constructed as `<comma-separated args> [<counter>]` where `counter` specifies the order
of execution.

**Check out `examples` folder for more examples!**