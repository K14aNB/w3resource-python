"""
Task
----
Write a python program to count the number of characters (character frequency) in a string.

Sample Input:
'google.com'

Output:
{'g':2, 'o':3, 'l':1, 'e':1, '.':1, 'c':1, 'm':1}
"""


def count_character_occurrence(string: str) -> dict[str, int]:
    """
    Function to count the occurrence of each character in a string.

    Arguments
    ---------
        string (str): Any string

    Returns
    -------
        occurrence (dict[str, int]): dictionary having unique characters as keys and the count of occurrence as values.
    """

    occurrence = {}

    for char in string:
        if char in occurrence.keys():
            occurrence[char] += 1
        else:
            occurrence[char] = 1

    return occurrence


if __name__ == "__main__":
    string = input("Enter string:")
    print(f"Character frequency of {string} = {
          count_character_occurrence(string)}")
