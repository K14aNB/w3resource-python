"""
Task
----
Write a python program to determine the profiling of Python programs.
"""

from cProfile import run


def sum(a: int, b: int) -> int:
    """
    Function to find the sum of two integers.

    Arguments
    ---------
        a (int): Any integer
        b (int): Any integer

    Returns
    -------
        sum (int): Sum of a and b.
    """

    sum = a + b

    return sum


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    run("sum(a, b)")
