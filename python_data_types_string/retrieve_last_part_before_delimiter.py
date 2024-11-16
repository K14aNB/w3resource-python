"""
Task
----
Write a python program to get the last part of a string before a specified character.

Sample Input:
'https://www.w3resource.com/python-exercises'
'-'

Output:
'https://www.w3resource.com/python'
"""


def retrieve_chars_before_delimiter(string: str, delim: str) -> str:
    """
    Function to retrieve the last part of a string before the delimiter.

    Arguments
    ---------
        string (str): Any string with a delimiter.
        delim (str): Delimiter. can be '-', '/', ',', '.', ';'

    Returns
    -------
        Substring of the string before the last occurrence of delimiter.\n
        If multiple delimiters of the specified type is present, \n
        only the last will be considered.
    """

    return string.rsplit(sep=delim, maxsplit=1)[0] if delim in string else string


if __name__ == "__main__":
    input_string = input("Enter string with delimiters:")
    delimiter = input("Enter delimiter:")

    print(f"Modified string = {
          retrieve_chars_before_delimiter(input_string, delimiter)}")
