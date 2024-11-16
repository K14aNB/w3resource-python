"""
Task
----
Write a python program to list files in current directory
"""

from os import listdir, getcwd
from os.path import isfile, join

files = [
    file
    for file in listdir(join(getcwd(), "python_basic_part-1"))
    if isfile(join(getcwd(), "python_basic_part-1", file))
]

print(files)
