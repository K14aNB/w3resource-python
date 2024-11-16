"""
Task
----
Write a python program to shuffle and print a specified list.
"""

from random import shuffle

input_list = input("Enter list items separated by commas:").split(",")

# Method 1
print(f"Shuffled list = {list(set(input_list))}")

# Method 2
shuffle(input_list)
print(f"Shuffled list = {input_list}")
