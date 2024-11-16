"""
Task
----
Write a python function that takes list of words and return the longest word and length of the longest word.

Sample Input:
['Hello', 'Hi', 'How']

Output:
'Hello', 5
"""


def longest_word(list_of_words: list[str]) -> tuple[str, int]:
    """
    Function to retrieve the longest word and length of the longest word from a list of words.

    Arguments
    ---------
        list_of_words (list[str]): A list of words.

    Returns
    -------
        longest (tuple[str, int]): A list of Longest word from `list_of_words` and it's length.
    """

    longest = list_of_words

    longest.sort(key=lambda x: len(x), reverse=True)

    return longest[0]


if __name__ == "__main__":
    input_list = map(str, input("Enter list of words separated by commas:").split(","))

    print(f"Longest = {longest_word(input_list)}")
