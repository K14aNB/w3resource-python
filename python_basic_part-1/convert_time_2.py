"""
Task
----
Write a python program that converts seconds into days, hours, minutes and seconds.
"""

from convert_time import convert_time


time = float(input("Enter time:"))
current = input("Enter current unit of time:")
to = input("Enter unit to convert time into:")

print(f"Time in {to} = {convert_time(current, to, time)}")
