"""
Task
----
Write a python program to get the size of an object in bytes.
"""

from sys import getsizeof

print(f"Object size of int = {getsizeof(10)}")
print(f"Object size of float = {getsizeof(10.0)}")
print(f"Object size of str = {getsizeof("Hi")}")
print(f"Object size of list = {getsizeof([10, 20.0, "Hi", True])}")
print(f"Object size of tuple = {getsizeof((10, 20.0, "Hi", True))}")
print(f"Object size of set = {getsizeof({10, 20.0, "Hi", True})}")
print(f"Object size of dict = {getsizeof(
    {"Hi": "Hello", "Name": "KB", "Age": 20})}")
