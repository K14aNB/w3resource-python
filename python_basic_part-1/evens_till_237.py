"""
Task
----
Write a python program to print all even numbers from a given list of numbers in the same order and stop printing any numbers after 237 in the sequence.

Sample Input:
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

Output:
even_numbers = [386, 462, 418, 344, 236, 566, 978, 328, 162, 758, 918]
"""


def even_nos(numbers: list[int]) -> list[int]:
    """
    Function to print even numbers present in the list in same order till 237.

    Arguments
    ---------
        numbers (list[int]): List of integers

    Returns
    -------
        even_numbers (list[int]): List of even numbers present in numbers till 237
    """

    even_nos = []

    for num in numbers:
        if num == 237:
            break
        elif num % 2 == 0:
            even_nos.append(num)

    return even_nos


if __name__ == "__main__":
    numbers = [
        386,
        462,
        47,
        418,
        907,
        344,
        236,
        375,
        823,
        566,
        597,
        978,
        328,
        615,
        953,
        345,
        399,
        162,
        758,
        219,
        918,
        237,
        412,
        566,
        826,
        248,
        866,
        950,
        626,
        949,
        687,
        217,
        815,
        67,
        104,
        58,
        512,
        24,
        892,
        894,
        767,
        553,
        81,
        379,
        843,
        831,
        445,
        742,
        717,
        958,
        743,
        527,
    ]
    print(even_nos(numbers))
