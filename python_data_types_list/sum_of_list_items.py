"""
Task
----
Write a python program to sum all items in a list.
"""


def sum_list_items(list_items: list[int]) -> float:
    """
    Function to find the sum of all list items.

    Arguments
    ---------
        list_items (list[int | float | bool]): List of items of types int, float or bool.

    Returns
    ------
        sum (float): Sum of `list_items`.
    """

    sum = 0

    for item in list_items:
        sum += item

    return sum


if __name__ == "__main__":
    list_items = list(
        map(int, input("Enter list items separated by commas:").split(","))
    )

    print(f"Sum of {list_items} = {sum_list_items(list_items)}")
