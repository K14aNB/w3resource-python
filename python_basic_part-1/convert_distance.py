"""
Task
----
Write a python program to convert distance from one unit to another.
"""


def convert_distance(
    current: str = "m", to: str = "km", distance: float = 1000.0
) -> float:
    """
    Function to convert distance from one unit to another unit.

    Arguments
    ---------
        current (str): Indicates the current unit the `distance` is given. Can take values like cm, centimeters, m, meters, in, inches, ft, feet, yds, yards, mi, miles. Default = m
        to (str): Indicates the unit `distance` is to be converted into. Can take values like cm, centimeters, m, meters, in, inches, ft, feet, yds, yards, mi, miles. Default = km
        distance (float): Distance in specific unit. Default = 1000.0

    Returns
    -------
        dist (float): Distance from `distance` converted to the unit as per value of `to`
    """

    dist = distance

    if to != current and current in [
        "cm",
        "centimeters",
        "m",
        "meters",
        "in",
        "inches",
        "ft",
        "feet",
        "yds",
        "yards",
        "mi",
        "miles",
    ]:
        match to.lower():
            case "cm" | "centimeters":
                if current in ["in", "inches"]:
                    dist *= 2.54
                elif current in ["ft", "feet"]:
                    dist *= 30.28
                elif current in ["m", "meters"]:
                    dist *= 100
                elif current in ["yds", "yards"]:
                    dist *= 91.44
                elif current in ["mi", "miles"]:
                    dist *= 160934

            case "m" | "meters":
                if current in ["cm", "centimeters"]:
                    dist /= 100
                elif current in ["in", "inches"]:
                    dist /= 39.37
                elif current in ["ft", "feet"]:
                    dist /= 3.28
                elif current in ["yds", "yards"]:
                    dist /= 1.094
                elif current in ["mi", "miles"]:
                    dist *= 1609.34

            case "in" | "inches":
                if current in ["cm", "centimeters"]:
                    dist /= 2.54
                elif current in ["ft", "feet"]:
                    dist *= 12
                elif current in ["m", "meters"]:
                    dist *= 39.37
                elif current in ["yds", "yards"]:
                    dist *= 36
                elif current in ["mi", "miles"]:
                    dist *= 63360

            case "ft" | "feet":
                if current in ["cm", "centimeters"]:
                    dist /= 30.28
                elif current in ["m", "meters"]:
                    dist *= 3.28
                elif current in ["in", "inches"]:
                    dist /= 12
                elif current in ["yds", "yards"]:
                    dist *= 3
                elif current in ["mi", "miles"]:
                    dist *= 5280

            case "yds" | "yards":
                if current in ["cm", "centimeters"]:
                    dist /= 91.44
                elif current in ["in", "inches"]:
                    dist /= 36
                elif current in ["ft", "feet"]:
                    dist /= 3
                elif current in ["m", "meters"]:
                    dist *= 1.094
                elif current in ["mi", "miles"]:
                    dist *= 1760

            case "mi" | "miles":
                if current in ["cm", "centimeters"]:
                    dist /= 160934
                elif current in ["in", "inches"]:
                    dist /= 63360
                elif current in ["ft", "feet"]:
                    dist /= 5280
                elif current in ["yds", "yards"]:
                    dist /= 1760
                elif current in ["m", "meters"]:
                    dist /= 1609.34

            case _:
                print("Invalid units")

    else:
        print("Please enter distance in valid unit")

    if dist != distance:
        return dist


if __name__ == "__main__":
    distance = float(input("Enter Distance:"))
    current = input("Enter current unit:")
    to = input("Enter the unit to be converted to:")

    print(f"Distance in {to} = {convert_distance(current, to, distance)}")
