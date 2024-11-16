"""
Task
----
Write a python program to find the list of words that are longer than n from a given list of words.
"""

input_list = list(
    map(str, input("Enter sequence of words separated by commas:").split(","))
)

limit = int(input("Enter limit:"))

output_list = [word for word in input_list if len(word) > limit]

print(f"Words in {input_list} that are greater than {limit} = {output_list}")
