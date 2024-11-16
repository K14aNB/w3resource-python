"""
Task
----
Write a python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

from math import sqrt


def calculate_distance(point_1: tuple[float], point_2: tuple[float]) -> float:
    """
    Function to calculate distance between point_1 and point_2.

    Arguments
    ---------
        point_1 (tuple[float]): Co-ordinates of point_1 (x1, y1)
        point_2 (tuple[float]): Co-ordinates of point_2 (x2, y2)

    Returns
    -------
        distance (float): Distance between point_1 and point_2.
    """

    x1 = point_1[0]
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]

    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return round(distance, 3)


if __name__ == "__main__":
    point_1 = tuple(map(float, input("Enter co-ordinates of point_1:").split(",")))
    point_2 = tuple(map(float, input("Enter co-ordinates of point_2:").split(",")))

    print(
        f"Distance between {point_1} and {point_2} = {
            calculate_distance(point_1, point_2)}"
    )
