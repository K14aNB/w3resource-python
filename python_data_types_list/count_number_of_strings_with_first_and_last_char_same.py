"""
Task
----
Write a python program to count the number of strings which satisfy the given condition.
The string should be of length 2 or more and first and last characters should be same.

Sample Input:
['abc', 'xyz', 'aba', '1221']

Output:
2
"""


def count_number_of_strings(list_of_strings: list[str]) -> int:
    """
    Function to count the number of strings in the list which satisfy given conditions.\n
    Conditions:\n
        - The strings should be of length 2 or more\n
        - The first and last characters of the string should be same.\n

    Arguments
    ---------
        list_of_strings (list[str]): A list of strings.

    Returns
    -------
        count (int): Number of strings in the list which satisfy the above conditions.
    """

    count = 0

    for string in list_of_strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1

    return count


if __name__ == "__main__":
    input_list = list(
        map(str, input("Enter sequence of strings separated by commas:").split(","))
    )

    print(f"Count of strings in {input_list} = {
          count_number_of_strings(input_list)}")
