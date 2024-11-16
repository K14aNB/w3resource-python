"""
Task
----
Write a python program to convert the bytes in given string to a list of integers.
"""


def convert_bytes_to_list_of_int(string: str) -> list[int]:
    """
    Function to convert bytes in a given string to list of integers.

    Arguments
    ---------
        bytes_str (str): Any string

    Returns
    -------
        byte_values (list[int]): List of integers corresponding to bytes in `bytes_str`.
    """

    bytes_str = bytes(string, encoding="utf-8")

    byte_values = list(bytes_str)

    return byte_values


if __name__ == "__main__":
    input_str = input()

    print(convert_bytes_to_list_of_int(input_str))
