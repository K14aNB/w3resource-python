"""
Task
----
Write a python program to count the occurrence of each word in a sentence.
"""


def count_word_occurrence(string: str) -> dict[str, int]:
    """
    Function to count occurrence of each word in a sentence.

    Arguments
    ---------
        string (str): Any sentence.

    Returns
    -------
        word_occurrence (dict[str, int]): dictionary of unique words in the sentence as keys and the count of occurrence of corresponding word as values.
    """

    list_of_words = string.split(" ")

    word_occurrence = {}

    for word in list_of_words:
        if word in word_occurrence.keys():
            word_occurrence[word] += 1
        else:
            word_occurrence[word] = 1

    return word_occurrence


if __name__ == "__main__":
    input_sentence = input("Enter a sentence:")

    print(f"Word occurrence in {input_sentence} = {
          count_word_occurrence(input_sentence)}")
