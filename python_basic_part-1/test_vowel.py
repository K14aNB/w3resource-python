"""
Task
----
Write a python program to test whether a passed letter is a vowel or not.
"""


def is_vowel(letter: str) -> bool:
    """
    Function to test whether a passed letter is a vowel or not

    Arguments
    ---------
        letter (str): Any character

    Returns
    -------
        True if letter is a vowel
        False if letter is not a vowel
    """

    return letter in ["a", "e", "i", "o", "u"]


if __name__ == "__main__":
    letter = input()
    if is_vowel(letter):
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is not a vowel")
