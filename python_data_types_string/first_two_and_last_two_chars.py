"""
Task
----
Write a python program to get a string made of first 2 and last 2 characters of a given string. If string length is less than 2, return empty string.

Sample Input:
'w3resource'

Output:
w3ce

Sample Input:
'w3'

Output:
'w3w3'

Sample Input:
'w'

Output:
''
"""

string = input("Enter string:")

first_two_and_last_two = string[:2] + string[-2:] if len(string) >= 2 else ""

print(f"First two and last two characters of {
    string} = {first_two_and_last_two}")
