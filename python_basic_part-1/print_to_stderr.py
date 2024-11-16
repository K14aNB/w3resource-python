"""
Task
----
Write a python program to print to STDERR.
"""

from __future__ import print_function
from sys import stderr


def eprint(*args, **kwargs):
    print(*args, **kwargs, file=stderr)


eprint("abc", "def", sep="--")
