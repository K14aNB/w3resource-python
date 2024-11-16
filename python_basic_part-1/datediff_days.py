"""
Task
----
Write a python program to calculate the number of days between two dates.

Sample Input:
(2014, 7, 2), (2014, 7, 11)

Output:
9 days
"""


def datediff_days(date_1: tuple[int], date_2: tuple[int]) -> int:
    """
    Function to calculate difference between two dates in number of days.

    Arguments
    ---------
        date_1 (tuple[int]): The date components should be in format yyyy, mm, dd and earlier date compared to date_2
        date_2 (tuple[int]): The date components should be in format yyyy, mm, dd and later date compared to date_1

    Returns
    -------
        Difference between date_1 and date_2 in number of days (int).
    """
    if date_1 == date_2:
        return 0
    else:
        date_3 = (date_2[0] - date_1[0], date_2[1] - date_1[1], date_2[2] - date_1[2])
        return 365 * date_3[0] + 30 * date_3[1] + date_3[2]


if __name__ == "__main__":
    date_1 = tuple(map(int, input("Enter Date 1 {yyyy,mm,dd}").split(",")))
    date_2 = tuple(map(int, input("Enter Date 2 {yyyy,mm,dd}").split(",")))
    print(f"{datediff_days(date_1, date_2)} days")
