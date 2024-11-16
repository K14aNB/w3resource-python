"""
Task
----
Write a python program to sort three numbers without using conditional statements or loops.
"""

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


# Method 1 - Using sorted
print(f"Sorted numbers using sorted = {sorted([num_1, num_2, num_3])}")

# Method 2 - Using min and max
print(f"Sorted numbers using min and max = {min(num_1, num_2, num_3), (num_1 + num_2 + num_3) - min(
    num_1, num_2, num_3) - max(num_1, num_2, num_3), max(num_1, num_2, num_3)}")
