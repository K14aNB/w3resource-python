"""
Task
----
Write a python program to add an item to a tuple.
"""

input_tuple = tuple(
    map(int, input("Enter sequence of numbers separated by commas:").split(","))
)
input_element = int(input("Enter element to be added to tuple:"))

print(f"Before Addition: {input_tuple}")

# Method 1
input_tuple = input_tuple + (input_element,)
print(f"After Addition: {input_tuple}")


# Method 2
input_list = list(input_tuple)

input_list.append(input_element)

print(f"After Addition: {tuple(input_list)}")
