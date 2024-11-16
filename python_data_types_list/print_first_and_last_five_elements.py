"""
Task
----
Write a python program to generate and print a list of first and last 5 elements where values are square numbers between 1 and 30 (both included).
"""

input = [x**2 for x in range(1, 31)]

print(f"First 5 elements in {input} = {input[:5]}")
print(f"Last 5 elements in {input} = {input[-5:]}")
