"""
Task
----
Write a python program to multiply all the items in a dictionary.
"""

dict_ex = {0: 5, 1: 10, 2: 20, 3: 30}

result = 1

for val in dict_ex.values():
    result *= val

print(result)
