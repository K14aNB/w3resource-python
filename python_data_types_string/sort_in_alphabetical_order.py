"""
Task
----
Write a python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form.

Sample Input:
'red', 'white', 'black', 'pink', 'green', 'black'

Output:
'black', 'green', 'pink', 'red', 'white'
"""

input_sequence = list(
    map(str, input("Enter sequence of words separated by commas:").split(","))
)

input_sequence.sort()

print(f"Sorted Sequence = {input_sequence}")
