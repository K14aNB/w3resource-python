"""
Task
----
Write a python function to get a string made of the first three characters of a specified string.
If the length of the string is less than 3, return the original string.

Sample Input:
first_three('ipy')

Output:
'ipy'
"""


def first_three(string: str) -> str:
    """
    Function to get a string made of the first three characters of a specified string.

    Arguments
    ---------
        string (str): Any string.

    Returns
    -------
        A string made of first three characters of `string`.
        If length of `string` is less than 3, `string` will be returned.
    """

    return string[:3] if len(string) >= 3 else string


if __name__ == "__main__":
    input_string = input("Enter string:")

    print(f"First three characters of {
          input_string} = {first_three(input_string)}")
