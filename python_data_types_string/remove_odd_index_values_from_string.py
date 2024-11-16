"""
Task
----
Write a python program to remove characters that have odd index values in a given string.
"""

input_string = input("Enter string:")

modified_string = "".join(
    [char for ind, char in enumerate(input_string) if ind % 2 == 0]
)

print(f"Modified string = {modified_string}")
