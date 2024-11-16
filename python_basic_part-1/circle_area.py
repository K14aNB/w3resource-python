"""
Task
----
Write a python program that calculates the area of a circle based on the radius entered by the user.

Sample Input:
r = 1.1

Output:
Area = 3.8013271108436504
"""

from math import pi


def circle_area(rad: float) -> float:
    """
    Function to calculate the area of a circle of radius rad

    Arguments
    ---------
        rad (float): Radius of the given circle

    Returns
    -------
        area (float): Area of the given circle
    """

    area = pi * rad**2

    return area


if __name__ == "__main__":
    rad = float(input())
    print(f"Area={circle_area(rad)}")
