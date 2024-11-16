"""
Task
----
Write a python program to create a clone of a tuple.
"""

from copy import deepcopy

input_tuple: tuple[str, int, list[int], bool] = ("Hello", 5, [], True)

print(id(input_tuple))

tuple_clone = deepcopy(input_tuple)

print(id(tuple_clone))

tuple_clone[2].append(2)

print(id(tuple_clone))

print(input_tuple)

print(tuple_clone)
