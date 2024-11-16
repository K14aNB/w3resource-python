"""
Task
----
Write a python program to calculate the hypotenuse of a right-angled triangle.
"""

from math import sqrt


def calculate_hypotenuse(base: float, height: float) -> float:
    """
    Function to calculate the hypotenuse of a right-angled triangle.

    Arguments
    ---------
        base (float): Base of the triangle
        height (float): Height of the triangle

    Returns
    -------
        hyp (float): Hypotenuse of the right-angled triangle of given base and height
    """

    hyp = sqrt(base**2 + height**2)

    return round(hyp, 3)


if __name__ == "__main__":
    base = float(input("Enter base of triangle:"))
    height = float(input("Enter height of triangle:"))

    print(
        f"Hypotenuse of triangle with {base} and {height} is {calculate_hypotenuse(base, height)}"
    )
