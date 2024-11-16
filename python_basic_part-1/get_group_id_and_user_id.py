"""
Task
----
Write a python program to get the effective group id, effective user id, real group id, and a list of supplemental group ids associated with the current process.
"""

from os import getgid, getegid, geteuid, getgroups

print(f"Effective group id = {getegid()}")

print(f"Effective user id = {geteuid()}")

print(f"Real group id = {getgid()}")

print(f"List of supplemental group ids = {getgroups()}")
