"""
Task
----
Write a python program to calculate the sum of first n positive integers.
"""


def sum_of_first_n_integers(n: int) -> int:
    """
    Arguments
    ---------
        n (int): Limit till which sum of numbers to be calculated.

    Returns
    -------
        sum (int): Sum of first n integers.
    """

    sum = 0

    for i in range(1, n + 1):
        sum += i

    return sum


if __name__ == "__main__":
    n = int(input("Enter limit (n):"))

    print(f"Sum of first {n} integers = {sum_of_first_n_integers(n)}")
