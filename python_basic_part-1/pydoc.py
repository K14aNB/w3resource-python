"""
Task
----
Write a python program to print the documentation (syntax, description etc.) of Python built-in functions.

Sample Input:
abs

Output:
abs(number) -> number
Return the absolute value of the argument.
"""

import builtins

function_name = input().removesuffix("()")

function = getattr(builtins, function_name)

print(function.__doc__)
