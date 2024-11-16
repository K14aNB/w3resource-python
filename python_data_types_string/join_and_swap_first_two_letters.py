"""
Task
----
Write a python program to get a single string from two given strings, separated by space and swap the first two characters of each string.

Sample Input:
'abc', 'xyz'

Output:
'xyc' 'abz'
"""


def join_and_swap_first_two(string_1: str, string_2: str) -> str:
    """
    Function to join two strings separated by space and swap the first two characters of each string.

    Arguments
    ---------
        string_1 (str): Any string
        string_2 (str): Any string

    Returns
    -------
        modified_string (str): string formed by joining `string_1` and `string_2` then swapping first two letters of each string.
    """

    modified_string = " ".join(
        [
            string_1.replace(string_1[:2], string_2[:2]),
            string_2.replace(string_2[:2], string_1[:2]),
        ]
    )

    return modified_string


if __name__ == "__main__":
    string_1 = input("Enter string_1:")
    string_2 = input("Enter string_2:")

    print(f"Modified String = {join_and_swap_first_two(string_1, string_2)}")
