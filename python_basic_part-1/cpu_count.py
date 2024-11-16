"""
Task
----
Write a python program to find out the number of CPUs used.
"""

from multiprocessing import cpu_count

print(cpu_count())
