"""
Task
----
Write a python program to print the numbers of a specified list after removing even numbers from it.
"""

input_list = list(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)

result_list = [x for x in input_list if x % 2 == 0]

print(f"Result list = {result_list}")
