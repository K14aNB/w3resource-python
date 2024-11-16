"""
Task
----
Write a python program to check if a list is empty or not.
"""

input_list = input().split()

# Method 1
if not input_list:
    print("Method 1 - List is empty")
else:
    print("Method 1 - List is not empty")


# Method 2
if len(input_list) > 0:
    print("Method 2 - List is not empty")
else:
    print("Method 2 - List is empty")
