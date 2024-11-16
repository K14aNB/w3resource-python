"""
Task
----
Write a python program to get the command-line arguments passed to the script (name of the script, number of arguments, arguments).
"""

from sys import argv


print(f"Name of Script = {argv[0]}")

print(f"Number of arguments = {len(argv) - 1}")

print(f"Arguments = {argv[1:]}")
