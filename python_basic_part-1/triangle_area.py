"""
Task
----
Write a python program that will accept the base and height of a triangle and compute it's area.
"""


def triangle_area(base: float, height: float) -> float:
    """
    Function to calculate the area of a triangle.

    Arguments
    ---------
        base (float): Base of a triangle
        height (float): Height of a triangle

    Returns
    -------
        area (float): Area of the given triangle
    """

    return (base * height) / 2


if __name__ == "__main__":
    base = float(input())
    height = float(input())
    print(f"Area = {triangle_area(base, height)}")
