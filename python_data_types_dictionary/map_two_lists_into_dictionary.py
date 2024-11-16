"""
Task
----
Write a python program to map two lists into a dictionary.
"""

list_1 = [0, 1, 2, 3, 4]
list_2 = [100, 200, 300, 400]

dict_ex = dict(zip(list_1, list_2))

print(dict_ex)
