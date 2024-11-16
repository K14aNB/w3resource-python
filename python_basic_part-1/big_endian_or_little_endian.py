"""
Task
----
Write a python program to test whether the system is a big-endian or a little-endian platform.
"""

from sys import byteorder

if byteorder == "big":
    print("Big-Endian Platform")

elif byteorder == "little":
    print("Little-Endian Platform")
