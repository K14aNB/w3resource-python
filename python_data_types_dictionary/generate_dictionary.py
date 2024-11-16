"""
Task
----
Write a python script to generate and print a dictionary that contains a number (1 to n) in the form of (x, x**2).

Sample Input:
n = 5

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def generate_dictionary(n: int) -> dict[int, int]:
    """
    Function to generate dictionary that contains number (1 to n) in the form (x, x**2).

    Arguments
    ---------
        n (int): Integer limit

    Returns
    -------
        result (dict[int, int]): Dictionary of the form {1: 1, 2: 4, ...n: n**2}
    """

    result = {x: x**2 for x in range(1, n + 1)}

    return result


if __name__ == "__main__":
    limit = int(input("Enter limit:"))

    print(f"Dictionary of {limit} = {generate_dictionary(limit)}")
