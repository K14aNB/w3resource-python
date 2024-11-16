"""
Task
----
Write a python function to reverse a string if it's length is a multiple of 4.
"""


def reverse_if_multiple_4(string: str) -> str:
    """
    Function to reverse a string if it's length is a multiple of 4.

    Arguments
    ---------
        string (str): Any string of length

    Returns
    -------
        Reversed string if length of `string` is a multiple of 4\n
        else returns `string`.
    """

    return string[::-1] if len(string) % 4 == 0 else string


if __name__ == "__main__":
    input_string = input("Enter string:")

    print(f"Modified string of {input_string} = {
          reverse_if_multiple_4(input_string)}")
