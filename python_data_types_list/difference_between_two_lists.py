"""
Task
----
Write a python program to calculate difference between two lists.
"""

list_1 = list(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)
list_2 = list(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)

list_12 = [x for x in list_1 if x not in list_2]
list_21 = [x for x in list_2 if x not in list_1]

print(f"Difference between {list_1} and {list_2} = {list_12 + list_21}")
