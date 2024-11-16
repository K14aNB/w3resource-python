"""
Task
----
Write a python program to divide a path by the extension separator.
"""

from os.path import splitext, expanduser, join

path = input("Enter path:")

if path.startswith("~"):
    path = join(expanduser("~"), path[2:])

separated_path = splitext(path)

print(f"Separated Path = {separated_path}")
