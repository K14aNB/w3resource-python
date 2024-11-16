"""
Task
----
Write a python function that takes two lists and returns True if they have at least one common element.
"""


def check_for_presence_of_common_element(list_1: list[int], list_2: list[int]) -> bool:
    """
    Function to check for the presence of a common element in two lists.

    Arguments
    ---------
        list_1 (list[int]): List of integers
        list_2 (list[int]): List of integers

    Returns
    -------
        True if there is a common element present else returns False.
    """

    set_1: set[int] = set(list_1)
    set_2: set[int] = set(list_2)

    return not set_1.isdisjoint(set_2)


if __name__ == "__main__":
    list_1 = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )
    list_2 = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )

    if check_for_presence_of_common_element(list_1, list_2):
        print(f"Common element is present in {list_1} and {list_2}")
    else:
        print(f"Common element is not present in {list_1} and {list_2}")
