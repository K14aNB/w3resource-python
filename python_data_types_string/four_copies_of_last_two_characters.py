"""
Task
----
Write a python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

Sample Input:
insert_end('Python')

Output:
'onononon'
"""


def insert_end(string: str) -> str:
    """
    Function to make 4 copies of the last two characters of a specified string.

    Arguments
    ---------
        string (str): Any string

    Returns
    -------
        A string made of 4 copies of last two characters of `string`.\n
        If length of `string` is less than 2, empty string will be returned.
    """

    return string[-2:] * 4 if len(string) >= 2 else ""


if __name__ == "__main__":
    input_string = input("Enter string:")

    print(f"Result = {insert_end(input_string)}")
