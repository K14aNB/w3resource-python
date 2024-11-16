"""
Task
----
Write a python program to create a symmetric difference.
"""

set_1: set[int | bool | str | float] = {10, 34.0, "Hi", True}
set_2: set[int | bool | str | float] = {10, "Hello", False, 34.0}
print(f"Symmetric Set Difference = {set_1.symmetric_difference(set_2)}")
