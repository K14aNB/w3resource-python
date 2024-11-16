"""
Task
----
Write a python program to print the current call stack.
"""

from traceback import print_stack


def abc():
    return print_stack()


def fun():
    return abc()


if __name__ == "__main__":
    fun()
