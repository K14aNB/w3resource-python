"""
Task
----
Write a python program to check whether a file path is a file or directory.
"""

from os.path import isfile, expanduser, join, abspath, exists

input = input("Enter path to check:")

if not input.startswith("/") and input.startswith("~"):
    path = join(expanduser(input[0]), input[2:])

elif not input.startswith("/"):
    path = abspath(input)

else:
    path = input

if exists(path):
    print(f"{path} is a file") if isfile(path) else print(f"{path} is a directory")

else:
    print(f"{path} does not exist.")
