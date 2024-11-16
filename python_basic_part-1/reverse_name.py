"""
Task
----
Write a python program that accepts the user's first name and last name prints them in reverse order with space between them.

Sample Input:
John Doe

Output:
Doe John
"""

first_name, last_name = map(str, input().split())

print(f"Reversed Name = {last_name} {first_name}")
