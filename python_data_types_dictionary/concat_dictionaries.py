"""
Task
----
Write a python script to concatenate the following dictionaries to create a new one.

Sample Input:
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}

Output:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}

result = dict_1.copy()
result.update(dict_2)
result.update(dict_3)

print(result)
