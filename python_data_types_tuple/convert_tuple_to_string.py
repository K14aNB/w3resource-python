"""
Task
----
Write a python program to convert a tuple to string.
"""

input_tuple = tuple(
    input("Enter sequence of characters separated by commas:").split(",")
)

print(f"String = {"".join(input_tuple)}")
