"""
Task
----
Write a python program to sum two given integers. However, if the sum is between 15 and 20, it will return 20.
"""


def sum_two(num_1: int, num_2: int) -> int:
    """
    Function to return the sum of two numbers.

    Arguments
    ---------
        num_1 (int): Any integer
        num_2 (int): Any integer

    Returns
    -------
        sum (int): Sum of two numbers. Returns 20 if sum is between 15 and 20
    """

    sum = num_1 + num_2

    if sum >= 15 and sum <= 20:
        sum = 20

    return sum


if __name__ == "__main__":
    num_1 = int(input())
    num_2 = int(input())

    print(f"Sum of {num_1} and {num_2} = {sum_two(num_1, num_2)}")
