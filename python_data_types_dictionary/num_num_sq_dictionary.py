"""
Task
----
Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are the square of keys.
"""

result = {x: x**2 for x in range(1, 16)}

print(result)
