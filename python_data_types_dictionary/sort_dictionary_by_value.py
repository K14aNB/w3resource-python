"""
Task
----
Write a python script to sort a dictionary by value.
"""

dict_ex = {"Roll": 1, "Number": 11, "Age": 26}

print(f"Dictionary sorted by values = {
      sorted(dict_ex.items(), key=lambda x: x[1])}")
