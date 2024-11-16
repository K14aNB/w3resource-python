"""
Task
----
Write a python program to get ASCII value of a character.
"""

char = input("Enter character:")
if len(char) == 1:
    print(f"ASCII value of {char} = {ord(char)}")
