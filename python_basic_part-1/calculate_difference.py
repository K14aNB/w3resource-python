"""
Task
----
Write a python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""


def calculate_difference(num: int) -> int:
    """
    Function to calculate difference between a given number and 17.

    Arguments
    ---------
        num (int): Any integer. This integer can be greater than, less than or equal to 17.

    Returns
    ------
        17 - num ; if num <= 17 else 2 * absolute value of (17 - num) ; if num > 17
    """
    if num <= 17:
        return 17 - num

    elif num > 17:
        return 2 * abs(17 - num)


if __name__ == "__main__":
    number = int(input())
    print(f"Difference = {calculate_difference(number)}")
