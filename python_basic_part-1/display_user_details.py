"""
Task
----
Write a python program that displays your name, age, and address on three different lines
"""


def user_details(name: str, age: int, address: str) -> None:
    """
    Function to display name, age, and address on three different lines

    Arguments
    ---------
        name (str): Name of the user
        age (int): Age of the user
        address (str): Address of the user

    Returns
    -------
        None
    """

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")


if __name__ == "__main__":
    name = input("Enter user name:")
    age = int(input("Enter user age:"))
    address = input("Enter user address:")

    user_details(name, age, address)
