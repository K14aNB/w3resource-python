"""
Task
----
Write a python program to add two objects if both objects are integers.
"""


def add_two_ints(
    num_1: int | float | str | bool, num_2: int | float | str | bool
) -> int:
    """
    Function to check and add two objects if both are integers.

    Arguments
    ---------
        num_1 (int | float | str | bool): Any integer, float, str or bool object
        num_2 (int | float | str | bool): Any integer, float, str or bool object

    Returns
    -------
        sum (int): Sum of num_1 and num_2 if both are integers else raises exception 'Both inputs must be of type int'
    """

    if type(num_1) is int and type(num_2) is int:
        return num_1 + num_2

    return "Both inputs must be of type int"


if __name__ == "__main__":
    print(f"Result = {add_two_ints(10, 20)}")
    print(f"Result = {add_two_ints(10.0, 20.0)}")
    print(f"Result = {add_two_ints('10', '20')}")
    print(f"Result = {add_two_ints(True, False)}")
