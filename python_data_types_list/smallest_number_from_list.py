"""
Task
----
Write a python program to get the smallest number from the list.
"""


def smallest_number(list_of_numbers: list[int]) -> int:
    """
    Function to get the smallest number from the list.

    Arguments
    ---------
        list_of_numbers (list[int]): List of integers.

    Returns
    -------
        Smallest number from `list_of_numbers`.
    """

    return sorted(list_of_numbers)[0]


if __name__ == "__main__":
    input_list = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )

    print(f"Smallest of {input_list} = {smallest_number(input_list)}")
