"""
Task
----
Write a python program to get the 4th element from the last element of a tuple.
"""

input_tuple = tuple(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)

print(f"4th element from last = {input_tuple[-4]}")
