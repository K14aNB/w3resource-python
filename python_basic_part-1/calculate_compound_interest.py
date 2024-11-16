"""
Task
----
Write a python program to compute the compound interest.

Sample Input:
amount = 10000
rate = 3.5
years = 7

Output:
12722.79
"""


def calculate_compound_interest(amount: float, rate: float, years: int) -> float:
    """
    Function to calculate compound interest.

    Arguments
    ---------
        amount (float): Principal amount
        rate (float): Rate of Interest
        years (int): Number of years

    Returns
    -------
        ci (float): Compound Interest
    """

    ci = amount * (1 + rate) ** years

    return ci


if __name__ == "__main__":
    amount = float(input("Enter Amount:"))
    rate = float(input("Enter Rate of interest:"))
    years = int(input("Enter Number of Years:"))

    print(
        f"Compound Interest (CI) = {
            calculate_compound_interest(amount, rate, years)}"
    )
