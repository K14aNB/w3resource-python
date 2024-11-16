"""
Task
----
Write a python program to calculate the body mass index.
"""


def calculate_bmi(weight: float, height: float) -> float:
    """
    Function to calculate the body mass index (bmi).

    Arguments
    ---------
        weight (float): Weight of the person in kg
        height (float): Height of the person in m

    Returns
    -------
        bmi (float): body mass index (bmi) of the person.
    """

    bmi = weight / height**2

    return round(bmi, 3)


if __name__ == "__main__":
    weight = float(input("Enter Weight in kg:"))
    height = float(input("Enter Height in m:"))

    print(f"Body Mass Index (bmi) = {calculate_bmi(weight, height)}")
