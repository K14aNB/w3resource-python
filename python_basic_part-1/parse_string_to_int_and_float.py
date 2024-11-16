"""
Task
----
Write a python program to parse a string to int and float.
"""

string = input()

print("Parsing {string} to int")

integer = int(string)

print(f"Integer value = {integer}")
print(f"Data type = {type(integer)}")

print("Parsing {string} to float")

float = float(string)

print(f"Float value = {float}")
print(f"Data type = {type(float)}")
