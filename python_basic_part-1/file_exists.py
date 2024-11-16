"""
Task
----
Write a python program to check whether a file exists.
"""

from os.path import isfile, abspath

file_name = input("Enter File name:")

print(f"{abspath(file_name)} exists") if isfile(file_name) else print(
    f"File - {file_name} does not exists"
)
