"""
Task
----
Write a python program to add 'ing' at the end of a given string (length should be atleast 3). If the given string already ends with 'ing', add 'ly' instead.
If the length of string is less than 3, leave it unchanged.

Sample Input:
'abc'

Output:
'abcing'

Sample Input:
'string'

Output:
'stringly'
"""

input_string = input("Enter any string:")

modified_string = (
    input_string
    if len(input_string) < 3
    else input_string + "ly"
    if input_string[-3:] == "ing"
    else input_string + "ing"
)

print(f"Modified string = {modified_string}")
