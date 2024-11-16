"""
Task
----
Write a python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""

from platform import architecture
from struct import calcsize

# Print Architecture
print(architecture()[0])


print(calcsize("P") * 8)
