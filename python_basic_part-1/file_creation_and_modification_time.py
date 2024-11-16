"""
Task
----
Write a python program that retrieves the date and time of file creation and modification.
"""

from time import ctime
from os.path import getctime, getmtime

print(f"File Creation Time = {ctime(getctime(__file__))}")

print(f"File Modification Time = {ctime(getmtime(__file__))}")
