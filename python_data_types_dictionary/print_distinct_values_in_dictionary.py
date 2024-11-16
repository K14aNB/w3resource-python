"""
Task
----
Write a python program to print all distinct values in a dictionary.

Sample Input:
[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

Output:
{'S005', 'S002', 'S007', 'S001', 'S009'}
"""


def print_distinct(list_of_dicts: list[dict[str, str]]) -> set[str]:
    """
    Function to print distinct values in a list of dictionaries.

    Arguments
    ---------
        list_of_dicts (list): List of dictionary

    Returns
    -------
        distinct_values (set[str]): A set of distinct values from the dictionary.
    """

    distinct_values = set()

    for dict in list_of_dicts:
        distinct_values.add(list(dict.values())[0])

    return distinct_values


if __name__ == "__main__":
    list_of_dicts = [
        {"V": "S001"},
        {"V": "S002"},
        {"VI": "S001"},
        {"VI": "S005"},
        {"VII": "S005"},
        {"V": "S009"},
        {"VIII": "S007"},
    ]

    print(f"Distinct values of {list_of_dicts} = {
          print_distinct(list_of_dicts)}")
