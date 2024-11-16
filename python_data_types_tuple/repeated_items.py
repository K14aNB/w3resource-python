"""
Task
----
Write a python program to find repeated items in a tuple.
"""

from collections import Counter


# Method 1 O(n)
def find_repeated_items(tuple_of_items: tuple[int, ...]) -> set[int] | None:
    """
    Function to find repeated items in a tuple.

    Arguments
    ---------
        tuple_of_items (tuple[int]): Tuple of integers which may be repeated.

    Returns
    -------
        Set of repeated items in `tuple_of_items`.\n
        If `tuple_of_items` contains only unique elements, return None
    """
    repeated_items: set[int] = set()
    seen_items: set[int] = set()

    for val in tuple_of_items:
        if val in seen_items:
            repeated_items.add(val)
        else:
            seen_items.add(val)

    return None if not repeated_items else repeated_items


# Method 2
def find_repeated_items_using_counter(
    tuple_of_items: tuple[int, ...],
) -> list[int] | None:
    """
    Function to find repeated items in a tuple.

    Arguments
    ---------
        tuple_of_items (tuple[int]): Tuple of integers which may be repeated.

    Returns
    -------
        list of repeated items in `tuple_of_items`.\n
        If `tuple_of_items` contains only unique elements, return None
    """

    repeated_items: list[int] = []

    for k, v in Counter(tuple_of_items).items():
        if v > 1:
            repeated_items.append(k)

    return None if not repeated_items else repeated_items


input_tuple: tuple[int, ...] = tuple(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)


print(f"Repeated items in {input_tuple} = {find_repeated_items(input_tuple)}")

print(f"Repeated items in {input_tuple} = {
      find_repeated_items_using_counter(input_tuple)}")
