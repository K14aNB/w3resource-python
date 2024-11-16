"""
Task
----
Write a python function to insert a string in the middle of another string.

Sample Input:
insert_string_middle('[[]]', 'Python')

Output:
'[[Python]]'
"""


def insert_string_middle(outer_string: str, inner_string: str) -> str:
    """
    Function to insert `inner_string` in the middle of `outer_string`.

    Arguments
    ---------
        outer_string (str): String which will be enclosing another string.
        inner_string (str): String to be inserted.

    Returns
    -------
        combined_string (str): Combined string of `outer_string` and `inner_string` with `inner_string` inserted in the middle.
    """

    combined_string = (
        outer_string[: len(outer_string) // 2]
        + inner_string
        + outer_string[len(outer_string) // 2 :]
    )

    return combined_string


if __name__ == "__main__":
    outer_string = input("Enter outer string:")
    inner_string = input("Enter inner string:")

    print(f"Combined string of {outer_string} and {inner_string} = {
          insert_string_middle(outer_string, inner_string)}")
