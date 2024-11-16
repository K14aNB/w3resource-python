"""
Task
----
Write a python program to display the current date and time

Sample Output:
Current date and time:
2024-10-15 15:55:34
"""

from datetime import datetime

print(datetime.today().strftime(format="%d-%m-%Y %H:%M:%S"))
