"""
Task
----
Write a python program to get the size of a file.
"""

from os.path import isfile, getsize, join, expanduser

file_path = input("Enter file path:")
if file_path.startswith("~"):
    file_path = join(expanduser("~"), file_path[2:])

if isfile(file_path):
    print(f"File size = {getsize(file_path)} bytes")
