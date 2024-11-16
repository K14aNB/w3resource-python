"""
Task
----
Write a python program to remove the nth index character from non-empty string
"""

input_string = input("Enter a string:")

input_index = int(input("Enter index to remove character:"))

modified_string = input_string[:input_index] + input_string[input_index + 1 :]

print(f"Modified string after removing {input_index} index character from {
      input_string} = {modified_string}")
