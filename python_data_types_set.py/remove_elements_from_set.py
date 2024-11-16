"""
Task
----
Write a python program to remove elements from a set.
"""

set_ex: set[int | float | str | bool] = {1, 22.0, "Hi", True}
set_ex.remove("Hi")
# set_ex.remove("Hello")
print(set_ex)
