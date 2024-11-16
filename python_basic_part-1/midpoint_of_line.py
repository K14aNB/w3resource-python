"""
Task
----
Write a python program to calculate midpoint of a line.
"""


def calculate_midpoint(p1: tuple[float], p2: tuple[float]) -> tuple[float]:
    """
    Function to calculate the midpoint of line between points p1 and p2.

    Arguments
    ---------
        p1 (tuple[int]): Point 1 of line with co-ordinates (x1, y1)
        p2 (tuple[int]): Point 2 of line with co-ordinates (x2, y2)

    Returns
    -------
        midpoint (tuple[int]): midpoint (x, y) of line between `p1` and `p2`
    """

    midpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    return midpoint


if __name__ == "__main__":
    point_1 = tuple(map(float, input().split(",")))
    point_2 = tuple(map(float, input().split(",")))

    print(f"Midpoint (x, y) of line between {point_1} and {
          point_2} = {calculate_midpoint(point_1, point_2)}")
