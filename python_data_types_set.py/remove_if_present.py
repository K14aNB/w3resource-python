"""
Task
----
Write a python program to remove an item from set, if it is present.
"""

set_ex: set[int | bool | float | str] = {10, True, 25.0, "Hi"}

set_ex.discard("HI")

print(set_ex)

set_ex.discard("Hi")
print(set_ex)
