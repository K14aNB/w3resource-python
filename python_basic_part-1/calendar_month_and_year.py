"""
Task
----
Write a python program that prints the calendar for a given month and year.
"""

import calendar

month = int(input("Enter month:"))
year = int(input("Enter year:"))

calendar.prmonth(theyear=year, themonth=month)
