"""
Task
----
Write a python program that computes the greatest common divisor (GCD) of two positive integers.
"""


def gcd(num_1: int, num_2: int) -> int:
    """
    Function to calculate the greatest common divisor (GCD) of two positive integers.

    Arguments
    ---------
        num_1 (int): Any positive integer
        num_2 (int): Any positive integer

    Returns
    -------
        gcd (int): greatest common divisor (GCD)
    """

    gcd = 1
    less = 0

    if num_1 == num_2:
        return num_1

    elif num_1 < num_2 == 0:
        if num_2 % num_1 == 0:
            return num_1
        else:
            less = num_1
    else:
        if num_1 % num_2 == 0:
            return num_2
        else:
            less = num_2

    for i in range(int(less / 2), 0, -1):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd = i
            break

    return gcd


if __name__ == "__main__":
    num_1 = int(input())
    num_2 = int(input())

    print(f"Greatest Common Divisor (GCD) of {num_1} and {num_2} = {gcd(num_1, num_2)}")
