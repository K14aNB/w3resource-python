"""
Task
----
Write a python program to clone or copy a list.
"""

from copy import copy, deepcopy

input_list = input("Enter list elements separated by commas:").split(",")

# Method 1 - Shallow copy
list_2 = input_list

# Method 2 - Shallow copy
list_3 = input_list.copy()

# Method 3 - Shallow copy
list_4 = [item for item in input_list]

# Method 4 - Shallow copy
list_5: list[str] = []
list_5.extend(input_list)

# Method 5 - Shallow copy
list_6: list[str] = []

for item in input_list:
    list_6.append(item)

# Method 6 - Shallow copy
list_7 = copy(input_list)

# Method 7 - Deep copy
list_8 = deepcopy(input_list)
