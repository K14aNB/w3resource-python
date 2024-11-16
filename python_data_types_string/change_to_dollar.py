"""
Task
----
Write a python program to get a string from a given string where all occurrences of it's first char have been changed to '$', except the first char itself.

Sample Input:
'restart'

Output:
'resta$t'
"""

string = input("Enter string:")

modified_string = string[0] + string[1:].replace(string[0], "$")

print(f"Modified String = {modified_string}")
