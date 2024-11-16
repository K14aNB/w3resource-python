"""
Task
----
Write a python program to generate all permutations of a list.
"""

from itertools import permutations

input_list = list(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)

print(f"Permutations of {input_list} = {list(permutations(input_list))}")
