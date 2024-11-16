"""
Task
----
Write a python program to combine two dictionary by adding values for common keys.
"""

from collections import Counter

# Method 1 O(n)


def combine_dict(dict_1: dict[str, int], dict_2: dict[str, int]) -> dict[str, int]:
    """
    Function to combine two dictionaries by adding values for common keys.

    Arguments
    ---------
        dict_1 (dict[str, int]): Dictionary
        dict_2 (dict[str, int]): Dictionary

    Returns
    -------
        combined (dict[str, int]): dictionary formed from combining `dict_1`and `dict_2` and adding values for common keys
    """

    combined = {}

    for key, value in dict_1.items():
        if key in dict_2.keys():
            combined[key] = dict_1[key] + dict_2[key]
        else:
            combined[key] = value

    for key, value in dict_2.items():
        if key not in dict_1.keys():
            combined[key] = value

    return combined


# Method 2


def combine_dict_counter(
    dict_1: dict[str, int], dict_2: dict[str, int]
) -> dict[str, int]:
    """
    Function to combine two dictionaries by adding values for common keys using Counter.

    Arguments
    ---------
        dict_1 (dict[str, int]): Dictionary
        dict_2 (dict[str, int]): Dictionary

    Returns
    -------
        combined_dict (dict[str, int]): dictionary formed from combining `dict_1` and `dict_2` and adding values for common keys.
    """

    return Counter(dict_1) + Counter(dict_2)


if __name__ == "__main__":
    dict_1 = {"a": 100, "b": 200, "c": 300}
    dict_2 = {"a": 300, "b": 200, "d": 400}

    print(f"Combined dictionary of {dict_1} and {
          dict_2} = {combine_dict(dict_1, dict_2)}")

    print(f"Combined dictionary of {dict_1} and {
          dict_2} = {combine_dict_counter(dict_1, dict_2)}")
