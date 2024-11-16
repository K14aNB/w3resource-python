"""
Task
----
Write a python program to get the current username.
"""

from getpass import getuser
from os import environ

# Method 1
print(getuser())

# Method 2
print(environ["HOME"].split("/")[2])
