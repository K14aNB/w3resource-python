"""
Task
----
Write a python program to create intersection of sets.
"""

set_1: set[int | float | bool | str] = {5, 22.0, "Hello", True}
set_2: set[int | float | bool | str] = {10, 24.0, "Hello", False}

print(f"Intersection of sets = {set_1.intersection(set_2)}")
