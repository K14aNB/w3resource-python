"""
Task
----
Write a python program that returns a string that is n (non-negative integer) copies of a string
"""


def string_ntimes(string: str, n: int) -> str:
    """
    Function to return string n times.

    Arguments
    ---------
        string (str): Any given string
        n (int): Number of times the given string is to be copied

    Returns
    -------
        The given string replicated n times.
    """

    return string * n


if __name__ == "__main__":
    string = input()
    n = int(input())
    print(string_ntimes(string, n))

    print(string * n)
