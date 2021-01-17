from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="recursion-tree-plotter",
    version="1.0.1",
    description="A Python package to plot the graph for calls to a recursive function",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikhilkumarsingh/recursion-tree-plotter",
    author="Nikhil Kumar Singh",
    author_email="nikhilksingh97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["recursion_tree_plotter"],
    include_package_data=True,
    install_requires=['pydot3']
)
