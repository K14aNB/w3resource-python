"""
Task
----
Write a python program to get the largest number from a list.
"""


def largest_number(list_of_numbers: list[int]) -> int:
    """
    Function to get the largest number from list of numbers.

    Arguments
    ---------
        list_of_numbers (list[int]): List of integers.

    Returns
    -------
        Largest number in `list_of_numbers`.
    """

    return sorted(list_of_numbers, reverse=True)[0]


if __name__ == "__main__":
    input_list = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )

    print(f"Largest number in {input_list} = {largest_number(input_list)}")
