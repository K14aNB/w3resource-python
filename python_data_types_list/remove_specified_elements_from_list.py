"""
Task
----
Write a python program to print a specified list after removing the 0th, 4th and 5th index elements.

Sample Input:
['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

Output:
['Green', 'White', 'Black']
"""

input_list = input("Enter elements separated by commas:").split(",")

result_list = [val for ind, val in enumerate(input_list) if ind not in [0, 4, 5]]

print(f"Resulting list = {result_list}")
