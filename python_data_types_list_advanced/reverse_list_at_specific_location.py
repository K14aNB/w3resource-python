"""
Task
----
Write a python function to reverse a list at a specific location.
"""


def reverse_in_loc(my_list: list[int], index_1: int, index_2: int) -> list[int]:
    """
    Function to reverse a list at a specific location.

    Arguments
    ---------
        my_list (list[int]): List of integers
        index_1 (int): Index of element in `my_list`
        index_1 (int): Index of element in `my_list`.

    Returns
    -------
        List of integers from `my_list` with elements at index_1 and index_2 reversed.
    """
    i = index_1
    j = index_2

    while i < j:
        my_list[i], my_list[j] = my_list[j], my_list[i]
        i += 1
        j -= 1

    return my_list


if __name__ == "__main__":
    input_list = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )
    index_1 = int(input("Enter index_1:"))
    index_2 = int(input("Enter index_2:"))

    print(f"{input_list} reversed at {index_1} to {index_2} = {
          reverse_in_loc(input_list, index_1, index_2)}")
