"""
Task
----
Write a python script to merge two python dictionaries.
"""

dict_1 = {"a": 100, "b": 200}
dict_2 = {"x": 100, "y": 200}

dict_3 = {}
dict_3.update(dict_1)
dict_3.update(dict_2)

print(dict_3)
