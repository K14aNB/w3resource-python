"""
Task
----
Write a python program to calculate the sum of the digits of a number.
"""


def calculate_sum_of_digits(num: int) -> int:
    """
    Function to calculate the sum of digits of a number.

    Arguments
    ---------
        num (int): Any integer

    Returns
    -------
        sum_of_digits (int): Sum of digits of `num`.
    """

    sum_of_digits = 0
    num_copy = num

    for _ in range(len(str(num_copy))):
        sum_of_digits += num_copy % 10
        num_copy //= 10

    return sum_of_digits


if __name__ == "__main__":
    num = int(input())

    print(f"Sum of digits of {num} = {calculate_sum_of_digits(num)}")
