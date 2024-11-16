"""
Task
----
Write a python program to check if a set is a subset of another set.
"""

set_1: set[int | bool | str | float] = {10, 55.0, True, "Hi"}
set_2: set[int | bool] = {10, True}
print(set_2.issubset(set_1))
print(set_1.issuperset(set_2))
