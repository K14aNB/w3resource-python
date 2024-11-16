"""
Task
----
Write a python program to test whether a number is within 100 of 1000 or 2000.
"""


def num_range(number: int) -> None:
    """
    Function to test whether a number is within 100 of 1000 or 2000

    Arguments
    ---------
        number (int): Any integer.

    Returns
    -------
        None
    """

    if (2000 - number) <= 100:
        print(f"{number} is within 100 of 2000")

    elif (1000 - number) <= 100:
        print(f"{number} is within 100 of 1000")

    else:
        print(f"{number} is not within 100 of 1000 or 2000")


if __name__ == "__main__":
    num = int(input())

    num_range(num)
