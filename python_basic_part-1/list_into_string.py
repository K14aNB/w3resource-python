"""
Task
----
Write a python program that concatenates all elements in a list into a string and returns it.
"""


def list_into_string(list_of_el: list[str]) -> str:
    """
    Task
    ----
    Function to concatenate all elements of a list into a string.

    Arguments
    ---------
        list_of_el (list[str]): List of elements

    Returns
    -------
        string_element (str): String formed as a result of concatenation of elements in list_of_el
    """

    string_element = ""

    for el in list_of_el:
        string_element += el

    return string_element


if __name__ == "__main__":
    list_of_elements = list(map(str, input().split(",")))
    print(list_into_string(list_of_elements))
