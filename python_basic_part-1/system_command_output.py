"""
Task
----
Write a python program to get system command output.
"""

from subprocess import run

command = input().split(",")

run(command)
