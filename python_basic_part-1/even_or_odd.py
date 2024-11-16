"""
Task
----
Write a python program that determines whether a given number (accepted from user) is even or odd, and prints an appropriate message to the user.
"""


def even_or_odd(num: int) -> str:
    """
    Function to determine whether a given number is even or odd.

    Arguments
    ---------
        num (int): Any integer

    Returns
    -------
        A message whether the given number is even or odd.
    """

    return "Even" if num % 2 == 0 else "Odd"


if __name__ == "__main__":
    print(even_or_odd(int(input())))
