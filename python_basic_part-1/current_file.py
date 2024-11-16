"""
Task
----
Write a python program to retrieve the path and name of the file currently being executed.
"""

from os.path import abspath, basename

print(abspath(__file__))
print(basename(__file__))
