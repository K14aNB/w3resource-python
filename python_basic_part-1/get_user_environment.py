"""
Task
----
Write a python program to get the user's environment.
"""

from pprint import pprint
from os import environ

pprint(dict(environ))
