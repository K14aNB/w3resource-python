"""
Task
----
Write a python program to get the hostname of the current system.
"""

from socket import gethostname
from platform import uname

# Method 1
print(gethostname())

# Method 2
print(uname()[1])
