"""
Task
----
Write a python program to swap two variables.
"""

x = input()
y = input()

print("Before Swap")
print(f"x={x} and y={y}")
print("After Swap")
x, y = y, x
print(f"x={x}, y={y}")
