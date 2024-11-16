"""
Task
----
Write a python program to calculate volume of sphere
"""

from math import pi


def volume_sphere(radius: float) -> float:
    """
    Function to calculate volume of sphere.

    Arguments
    ---------
        radius (float): Radius of the sphere

    Returns
    -------
        volume (float): Volume of the sphere
    """
    return (4 * pi * radius**3) / 3


if __name__ == "__main__":
    rad = float(input())
    print(f"Volume = {volume_sphere(rad)}")
