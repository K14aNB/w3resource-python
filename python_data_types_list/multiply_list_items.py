"""
Task
----
Write a python program to multiply all items in a list.
"""


def multiply_list_items(list_items: list[int]) -> float:
    """
    Function to multiply the list items.

    Arguments
    ---------
        list_items (list[int | float | bool]): List of items of types int, float or bool.

    Returns
    -------
        multiply (float): Multiplication of `list_items`.
    """

    multiply = 1

    for item in list_items:
        multiply *= item

    return multiply


if __name__ == "__main__":
    list_items = list(
        map(int, input("Enter list items separated by commas:").split(","))
    )
    print(f"Multiplication of {list_items} = {
          multiply_list_items(list_items)}")
