"""
Task
----
Write a python program to unpack a tuple into several variables.
"""

input_tuple = tuple(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)


n1, n2, n3, *n4 = input_tuple


print(n1)
print(n2)
print(n3)
print(n4)
