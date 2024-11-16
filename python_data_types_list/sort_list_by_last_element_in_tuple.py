"""
Task
----
Write a python program to get a list, sorted in increasing order by last element in each tuple from a given list of non-empty tuples.

Sample Input:
[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

Output:
[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

limit = int(input("Enter number of elements to be added to the list:"))
input_list: list[tuple[int]] = []
for _ in range(limit):
    input_list.append(
        tuple(
            map(
                int,
                input(
                    "Enter list element as tuple with integer elements separated by commas:"
                ).split(","),
            )
        )
    )

print(f"{input_list} sorted by last element in each tuple = {
      sorted(input_list, key=lambda x: x[-1])}")
