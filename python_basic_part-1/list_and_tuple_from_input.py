"""
Task
----
Write a python program that accepts a sequence of comma-separated numbers from the user and generates a list and tuple of those numbers.

Sample Input:
3, 5, 7, 23

Output:
List: ['3', '5', '7', '23']
Tuple: ('3', '5', '7', '23')
"""

inputs = input()
list_of_inputs = inputs.split(",")
tuple_of_inputs = tuple(inputs.split(","))

print(f"List: {list_of_inputs}\nTuple: {tuple_of_inputs}")
