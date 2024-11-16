"""
Task
----
Write a python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""


def sum_three(num_1: int, num_2: int, num_3: int) -> int:
    """
    Function to return the sum of three numbers.

    Arguments
    ---------
        num_1 (int): Any integer
        num_2 (int): Any integer
        num_3 (int): Any integer

    Returns
    -------
        sum (int): Sum of num_1, num_2, num_3. Returns zero if num_1 = num_2 or num_2 = num_3 or num_1 = num_3
    """

    sum = 0
    if num_1 != num_2 != num_3:
        sum = num_1 + num_2 + num_3

    return sum


if __name__ == "__main__":
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    print(f"Sum of {num_1}, {num_2}, {num_3} = {sum_three(num_1, num_2, num_3)}")
