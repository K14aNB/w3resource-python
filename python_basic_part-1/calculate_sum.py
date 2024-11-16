"""
Task
----
Write a python program to calculate the sum of three numbers. If the values are equal, return 3 times their sum.
"""


def calculate_sum(num_1: float, num_2: float, num_3: float) -> float:
    """
    Function to calculate the sum of 3 numbers.

    Arguments
    ---------
        num_1 (float): Any floating point number
        num_2 (float): Any floating point number
        num_3 (float): Any floating point number

    Returns
    -------
        3 times the sum if num_1 = num_2 = num_3 else num_1 + num_2 + num_3
    """
    if num_1 == num_2 == num_3:
        return 9 * num_1
    else:
        return num_1 + num_2 + num_3


if __name__ == "__main__":
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())

    print(f"Sum = {calculate_sum(num_1, num_2, num_3)}")
