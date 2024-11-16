"""
Task
----
Write a python program to count the occurence of a given number in a list.
"""


def count_occurrence(list_num: list[int], num: int) -> int:
    """
    Function to count the occurrence of a given number in a list.

    Arguments
    ---------
        list_num (list[int]): A list of integers
        num (int): Any integer

    Returns
    -------
        Count of occurrence of the num in list_num.
    """

    return list_num.count(num)


if __name__ == "__main__":
    list_of_nums = list(map(int, input().split(",")))
    num = int(input())
    print(count_occurrence(list_of_nums, num))
