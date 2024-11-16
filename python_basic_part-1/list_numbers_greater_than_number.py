"""
Task
----
Write a python program to test whether all numbers in a list are greater than a certain number.
"""


def check_if_elements_greater(list_num: list[float], num: float) -> bool:
    """
    Function to check if list elements are greater than the given number.

    Arguments
    ---------
        list_num (list[float]): List of floating point numbers.
        num (float): Any floating point number

    Returns
    -------
        True if the `list_num` elements are greater than `num` else False
    """

    for el in list_num:
        if el < num:
            return False

    return True


def check_all_elements_greater(list_num: list[float], num: float) -> bool:
    """
    Function to check if list elements are greater than the given number using all().

    Arguments
    ---------
        list_num (list[float]): List of floating point numbers.
        num (float): Any floating point number

    Returns
    -------
        True if the `list_num` elements are greater than `num` else False
    """

    return all(i > num for i in list_num)


if __name__ == "__main__":
    list_num = list(map(float, input("Enter list elements:").split(",")))
    num = float(input("Enter number to compare:"))

    # Method 1
    print("List elements are all greater than the number") if check_if_elements_greater(
        list_num, num
    ) else print("List elements are all not greater than the number")

    # Method 2
    print(
        "List elements are all greater than the number"
    ) if check_all_elements_greater(list_num, num) else print(
        "List elements are all not greater than the number"
    )
