"""
Task
----
Write a python program that calls an external command.
"""

from subprocess import run

print("Running ls command")
run(["ls", "-la"])
