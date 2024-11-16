"""
Task
----
Write a python program to check if each number is prime in a given list of numbers.
Return True if all numbers are prime otherwise False.

Sample Input:
[0, 3, 4, 7, 9]

Output:
False

Sample Input:
[3, 5, 7, 13]

Output:
True

Sample Input:
[1, 5, 3]

Output:
False
"""


def is_prime(number: int) -> bool:
    """
    Function to check whether given number is a prime number or not.

    Arguments
    ---------
        number (int): Any integer.

    Returns
    -------
        True if given number is a prime number else False
    """

    if number <= 1:
        return False
    else:
        i = 2
        while i <= number // 2:
            if number % i == 0:
                return False
            i += 1

        return True


def check_prime(list_of_nums: list[int]) -> bool:
    """
    Function to check whether the given list consist of prime numbers.

    Arguments
    ---------
        list_of_nums (list[int]): List of integers.

    Returns
    -------
        True if all the numbers in `list_of_nums` are prime numbers else returns False
    """

    return all([is_prime(x) for x in list_of_nums])


if __name__ == "__main__":
    input_list = list(
        map(int, input("Enter sequence of numbers separated by commas:").split(","))
    )

    if check_prime(input_list):
        print(f"All numbers in {input_list} are prime")
    else:
        print(f"All numbers in {input_list} are not prime")
