"""
Task
----
Write a python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' with 'good'.
Return the resulting string.

Sample Input:
'The lyrics is not that poor!'
'The lyrics is poor!'

Output:
'The lyrics is good!'
'The lyrics is poor!'
"""


def replace_not_poor(string: str) -> str:
    """
    Function to replace first occurrence of substring 'not'...'poor' with 'good'.

    Arguments
    ---------
        string (str): Any string.

    Returns
    -------
        Modified string of `string` with first occurrence of substring 'not'...'poor' replaced with 'good'\n
        If not and poor does not exist, returns the original string.

    """

    try:
        if string.find("not") < string.find("poor"):
            modified_string = string.replace(
                string[string.find("not") : string.find("poor") + 4], "good", 1
            )
            return modified_string

    except ValueError:
        print("not and poor does not exist")

    return string


if __name__ == "__main__":
    input_string = input("Enter string:")

    print(f"Modified String = {replace_not_poor(input_string)}")
