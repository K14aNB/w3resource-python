"""
Task
----
Write a python program to remove duplicates from a list.
"""

# Method 1


def remove_duplicates_using_sets(my_list: list[int]) -> list[int]:
    """
    Function to remove duplicates using sets.

    Arguments
    ---------
        my_list (list[int]): List of integers with duplicates.

    Returns
    -------
        List of integers with duplicates removed.\n
        Order of original list is not preserved.
    """

    return list(set(my_list))


# Method 2
def remove_duplicates_using_list_comprehension(my_list: list[int]) -> list[int]:
    """
    Function to remove duplicates using list comprehension.

    Arguments
    ---------
        my_list (list[int]): List of integers with duplicates.

    Returns
    -------
        List of integers with duplicates removed.\n
        Order of the original list is preserved.\n
        Inefficient for large lists.
    """

    result: list[int] = []

    [result.append(el) for el in my_list if el not in result]

    return result


# Method 3
def remove_duplicates_using_dict(my_list: list[int]) -> list[int]:
    """
    Function to remove duplicates using dict.

    Arguments
    ---------
        my_list (list[int]): List of integers with duplicates.

    Returns
    -------
        List of integers with duplicates removed.\n
        Order of the original list is preserved.\n
        Efficient for large lists.
    """

    return list(dict.fromkeys(my_list))


if __name__ == "__main__":
    my_list = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )

    # Using Method 1
    print(f"Removing duplicates from {my_list} using Method 1 = {
          remove_duplicates_using_sets(my_list)}")

    # Using Method 2
    print(f"Removing duplicates from {my_list} using Method 2 = {
          remove_duplicates_using_list_comprehension(my_list)}")

    # Using Method 3
    print(f"Removing duplicates from {my_list} using Method 3 = {
          remove_duplicates_using_dict(my_list)}")
