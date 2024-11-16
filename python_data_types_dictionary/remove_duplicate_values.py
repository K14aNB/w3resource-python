"""
Task
----
Write a python program to remove duplicates from the dictionary.
"""

# Method 1 Time complexity - O(n)


def remove_duplicates(
    dict_ex: dict[str, dict[str, list[str]]],
) -> dict[str, dict[str, list[str]]]:
    """
    Function to remove duplicate values in `dict_ex`.

    Arguments
    ---------
        dict_ex (dict[str, dict[str, list[str]]]): Dictionary which may contain duplicate values.

    Returns
    -------
        modified_dict (dict[str, dict[str, list[str]]]): Modified dictionary after removing duplicate values from `dict_ex`.
    """

    modified_dict_ex = {}
    seen_values = []

    for key, values in dict_ex.items():
        if values not in seen_values:
            seen_values.append(values)
            modified_dict_ex[key] = values

    return modified_dict_ex


if __name__ == "__main__":
    dict_ex = {
        "id1": {
            "name": ["Sara"],
            "class": ["V"],
            "subject_integration": ["english, math, science"],
        },
        "id2": {
            "name": ["David"],
            "class": ["V"],
            "subject_integration": ["english, math, science"],
        },
        "id3": {
            "name": ["Sara"],
            "class": ["V"],
            "subject_integration": ["english, math, science"],
        },
        "id4": {
            "name": ["Surya"],
            "class": ["V"],
            "subject_integration": ["english, math, science"],
        },
    }

    print(f"Modified dictionary after removing duplicate values from {
          dict_ex} using loops = {remove_duplicates(dict_ex)}")
