"""
Task
----
Write a python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""


def is_equal_or_sum_difference(num_1: int, num_2: int) -> bool:
    """
    Function to check if two numbers are equal or their sum or difference is 5.

    Arguments
    ---------
        num_1 (int): Any integer
        num_2 (int): Any integer

    Returns
    -------
        True if num_1 = num_2 or num_1 + num_2 = 5 or num_1 - num_2 = 5 else False
    """

    return num_1 == num_2 or num_1 + num_2 == 5 or num_1 - num_2 == 5


if __name__ == "__main__":
    num_1 = int(input())
    num_2 = int(input())

    print(f"Result of {num_1} and {num_2} = {
          is_equal_or_sum_difference(num_1, num_2)}")
