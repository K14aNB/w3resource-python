"""
Task
----
Write a python program to add elements to a set.
"""

set_ex: set[int | float | bool | str] = {1, 22.0, True, "Hi"}
print(set_ex)
set_ex.add("Hello")
print(set_ex)
