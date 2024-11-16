"""
Task
----
Write a python program to check if a dictionary is empty or not.
"""

dict_ex = {}

# Method 1
print(f"{dict_ex} is empty") if not dict_ex else print(f"{dict_ex} is not empty")


# Method 2
print(f"{dict_ex} is empty") if len(dict_ex) == 0 else print(f"{dict_ex} is not empty")
