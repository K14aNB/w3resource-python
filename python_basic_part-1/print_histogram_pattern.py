"""
Task
----
Write a python program to create a histogram pattern from a given list of integers
"""


def print_histogram(list_num: list[int]) -> None:
    """
    Function to print histogram from a given list of integers

    Arguments
    ---------
        list_num (list[int]): A List of integers

    Returns
    -------
        None
    """

    for num in list_num:
        print("*" * num)


if __name__ == "__main__":
    list_num = list(map(int, input().split(",")))
    print_histogram(list_num)
