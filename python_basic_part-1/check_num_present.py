"""
Task
----
Write a python program that checks whether a specified value is contained within a group of values.

Sample Input:
[1, 5, 8, 3]
3

Output:
True
"""


def is_num_present(list_num: list[int], num: int) -> bool:
    """
    Function to check if a given number is present in the list.

    Arguments
    ---------
        list_num (list[int]): A list of integers
        num (int): Any integer

    Returns
    -------
        True if num is present in the list
        False if num is not present in the list
    """

    return num in list_num


if __name__ == "__main__":
    list_num = list(map(int, input().split(",")))
    num = int(input())

    if is_num_present(list_num, num):
        print(f"{num} is present in {list_num}")
    else:
        print(f"{num} is not present in {list_num}")
