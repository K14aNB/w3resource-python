"""
Task
----
Write a python program to get a dictionary from object's fields
"""


class Dictionary:
    def __init__(self) -> None:
        self.x = 100
        self.y = 200
        self.z = 300


dict_obj = Dictionary()

print(dict_obj.__dict__)
