"""
Task
----
Write a python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2.
"""


def string_first2_ntimes(string: str, n: int) -> str:
    """
    Function to return first two characters of a given string.

    Arguments
    ---------
        string (str): Any given string
        n (int): Number of times the first two characters is to be copied

    Returns
    -------
        First two characters n times; if length of string >= 2
        else; string n times
    """

    return (string[:2] * n) if len(string) >= 2 else (string * n)


if __name__ == "__main__":
    string = input()
    n = int(input())
    print(string_first2_ntimes(string, n))
