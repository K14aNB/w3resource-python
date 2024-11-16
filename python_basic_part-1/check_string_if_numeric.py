"""
Task
----
Write a python program to check whether a string is numeric
"""

string = input()

try:
    float(string)
    print("Numeric")

except ValueError:
    print("Not Numeric")
