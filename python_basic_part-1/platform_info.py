"""
Task
----
Write a python program to get OS name, platform and release information
"""

from os import name
from platform import system, release


print(f"OS = {name}")
print(f"Platform = {system()}")
print(f"Release = {release()}")
