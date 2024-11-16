"""
Task
----
Write a python program to access the index of a list.
"""

input_list = list(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)

for ind, val in enumerate(input_list):
    print(f"{ind} -> {val}")
