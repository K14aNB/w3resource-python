"""
Task
----
Write a python program to check whether an element exists in a tuple.
"""

input_tuple = tuple(
    map(int, input("Enter sequence of ~numbers separated by commas:").split(","))
)
input_num = int(input("Enter Number:"))

if input_num in input_tuple:
    print(f"{input_num} exists in {input_tuple}")
else:
    print(f"{input_num} does not exist in {input_tuple}")
