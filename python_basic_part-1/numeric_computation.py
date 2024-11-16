"""
Task
----
Write a python program that accepts an integer (n) and computes the value of n+nn+nnn

Sample Input:
5

Output:
615
"""

input_num = input()

print(
    int(input_num) + int(input_num + input_num) + int(input_num + input_num + input_num)
)
