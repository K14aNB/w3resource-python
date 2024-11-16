"""
Task
----
Write a python program to sort the files in home directory by date
"""

from glob import glob
from os.path import getmtime, expanduser, join

files = glob(join(expanduser("~"), "*.png"))

sorted_files = sorted(files, key=getmtime)
print(files, end="\n")
