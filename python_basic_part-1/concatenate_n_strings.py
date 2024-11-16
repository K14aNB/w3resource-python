"""
Task
----
Write a python program to concatenate n strings.
"""

n = int(input("Enter limit:"))
n_strings = []

for i in range(1, n + 1):
    n_strings.append(input(f"Enter string-{i}:"))

print(f"Concatenated strings from {n_strings} = {" ".join(n_strings)}")
