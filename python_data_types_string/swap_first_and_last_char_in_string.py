"""
Task
----
Write a python program to change a given string to a newly formed string where the first and last characters have been exchanged.
"""

input_string = input("Enter a string:")

modified_string = input_string[-1] + input_string[1:-1] + input_string[0]

print(f"Modified String = {modified_string}")
