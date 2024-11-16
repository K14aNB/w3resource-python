"""
Task
----
Write a python program to get the execution time of a Python function.
"""

from time import time


def sum(a: int, b: int) -> int:
    """
    Function to calculate the sum of two integers.

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

    start_time = time()

    print(sum(a, b))

    end_time = time()

    print(f"Total time taken = {round(end_time - start_time, 3)}secs")
