"""
Task
----
Write a python program to create a union of sets.
"""

set_1: set[int | bool | str | float] = {22.0, True, 4, "Hi"}
print(set_1)
set_2: set[int | bool | str | float] = {21.0, False, 6, "Hello"}
print(set_2)
print(set_1.union(set_2))
