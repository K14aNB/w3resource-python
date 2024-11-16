"""
Task
----
Write a python program to sort a given dictionary by key.
"""

dict_ex = {2: 200, 5: 500, 1: 700, 4: 100, 3: 300}

print(dict(sorted(dict_ex.items(), key=lambda x: x[0])))
