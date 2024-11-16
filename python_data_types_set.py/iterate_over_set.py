"""
Task
----
Write a python program to iterate over sets.
"""

set_1: set[int | float | bool | str] = {1, 2.0, True, "Hello"}

# Iterating over set_1
for el in set_1:
    print(el)


# Iterating over set_1
list_1 = list(set_1)
for i in range(len(list_1)):
    print(list_1[i])
