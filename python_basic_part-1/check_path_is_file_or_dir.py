"""
Task
----
Write a python program to find the path to a file or directory when you encounter a path name.
"""

from os.path import expanduser, join, isabs

path = input("Enter path:")

if path.startswith("~"):
    path = join(expanduser("~"), path[2:])

print(f"Is {path} absolute path? - {isabs(path)}")
