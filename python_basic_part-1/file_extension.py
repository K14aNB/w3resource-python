"""
Task
----
Write a python program that accepts a filename from the user and prints the extension of the file.
"""

filename = input()

print(f"Extension = {filename.split('.')[1]}")
