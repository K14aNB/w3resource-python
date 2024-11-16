"""
Task
----
Write a python program to iterate over dictionaries using for loops.
"""

dict_ex = {0: 100, 1: 200, 2: 300, 3: 400}

for key, value in dict_ex.items():
    print(f"{key} -> {value}")
