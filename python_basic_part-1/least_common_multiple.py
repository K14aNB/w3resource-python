"""
Task
----
Write a python program to find the least common multiple (LCM) of two positive integers.
"""


def lcm(num_1: int, num_2: int) -> int:
    """
    Function to calculate the least common multiple (LCM) of two positive integers.

    Arguments
    ---------
        num_1 (int): Any positive integer
        num_2 (int): Any positve integer

    Returns
    -------
        lcm (int): least common multiple (LCM)
    """

    lcm = 0
    great = 0

    if num_1 == num_2:
        return num_1
    elif num_1 > num_2:
        if num_1 % num_2 == 0:
            return num_1
        else:
            great = num_1
    else:
        if num_2 % num_1 == 0:
            return num_2
        else:
            great = num_2

    while True:
        if great % num_1 == 0 and great % num_2 == 0:
            lcm = great
            break
        great += 1

    return lcm


if __name__ == "__main__":
    num_1 = int(input())
    num_2 = int(input())

    print(f"Least Common Multiple (LCM) of {num_1} and {num_2} = {lcm(num_1, num_2)}")
