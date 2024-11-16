"""
Task
----
Write a python program to count the number of occurrences of a character in a string.
"""


def count_occurence(string: str, char: str) -> int:
    """
    Function to count the number of occurrences of a character in a string.

    Arguments
    ---------
        string (str): Any string
        char (str): Any character

    Returns
    -------
        count (int): Count of occurrences of `char` in `string`.
    """

    count = 0

    if char in string:
        count += string.count(char)

    return count


if __name__ == "__main__":
    string = input("Enter any string:")
    char = input("Enter any char:")
    if len(char) == 1:
        print(f"Count of Occurrences of {char} in {
            string} = {count_occurence(string, char)}")
    else:
        char = input("Please enter a single character:")
