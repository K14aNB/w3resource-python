"""
Write a python program to create set difference.
"""

set_1: set[int | bool | str | float] = {5, 26.0, True, "Hello"}
print(set_1)
set_2: set[int | bool | str | float] = {6, 27.0, False, "Hello"}
print(set_2)

print(f"Set difference = {set_1.difference(set_2)}")
