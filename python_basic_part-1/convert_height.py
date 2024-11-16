"""
Task
----
Write a python program to convert height from one unit to another.
"""


def convert_height(current: str = "in", to: str = "cm", height: float = 1.0) -> float:
    """
    Function to convert height from one unit to another unit.

    Arguments
    ---------
        current (str): Indicates the current unit in which `height` is given. Can take values like cm, centimeters, m, meters, in, inches, feet, ft. Default = in
        to (str): Indicates unit the `height` is to be converted into. Can take values like cm, centimeters, m, meters, in, inches, feet, ft. Default = cm
        height (float): Height in specific unit. Default = 1.0

    Returns
    -------
        ht (float): Height from `height` converted to the unit as per value of `to`.
    """

    ht = height

    if to != current and current in [
        "cm",
        "centimeters",
        "m",
        "meters",
        "in",
        "inches",
        "ft",
        "feet",
    ]:
        match to.lower():
            case "cm" | "centimeters":
                if current in ["in", "inches"]:
                    ht *= 2.54
                elif current in ["ft", "feet"]:
                    ht *= 30.28
                elif current in ["m", "meters"]:
                    ht *= 100

            case "in" | "inches":
                if current in ["cm", "centimeters"]:
                    ht /= 2.54
                elif current in ["ft", "feet"]:
                    ht *= 12
                elif current in ["m", "meters"]:
                    ht *= 39.37

            case "ft" | "feet":
                if current in ["cm", "centimeters"]:
                    ht /= 30.28
                elif current in ["in", "inches"]:
                    ht /= 12
                elif current in ["m", "meters"]:
                    ht *= 3.28

            case "m" | "meters":
                if current in ["cm", "centimeters"]:
                    ht /= 100
                elif current in ["in", "inches"]:
                    ht /= 39.37
                elif current in ["ft", "feet"]:
                    ht /= 3.28

            case _:
                print("Invalid unit")
    else:
        print("Please enter height in valid unit")

    if ht != height:
        return ht


if __name__ == "__main__":
    height = float(input("Enter height:"))
    current = input("Enter the current unit:")
    to = input("Enter the unit to be converted to:")

    print(f"Height in {to} = {convert_height(current, to, height)}")
