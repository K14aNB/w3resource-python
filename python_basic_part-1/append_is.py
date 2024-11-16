"""
Task
----
Write a python program to get a newly-generated string from a given string where 'is' has been added to the front.
Return the string unchanged if the given string already begins with 'is'
"""


def append_is(string: str) -> str:
    """
    Function to check and append 'is' to a given string.

    Arguments
    ---------
        string (str): Any given string

    Returns
    -------
        Updated string with 'is' appended if not already present.
    """

    if string.startswith("is"):
        return string
    else:
        return "is" + string


if __name__ == "__main__":
    string = input()
    print(append_is(string))
