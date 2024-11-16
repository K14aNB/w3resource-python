"""
Task
----
Write a python program to find out what version of python you are using.
"""

from subprocess import run, CalledProcessError
import sys

# System Python Version
print(sys.version)
print(sys.version_info)

# Virtual env Python Version
try:
    run(["python", "--version"])

except CalledProcessError as e:
    print(f"{e.cmd} failed")
