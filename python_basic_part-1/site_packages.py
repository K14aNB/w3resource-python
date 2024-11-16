"""
Task
----
Write a python program to locate Python site packages.
"""

from site import getsitepackages

print(f"Site Packages = {getsitepackages()}")
