"""
Task
----
Write a python program to extract the filename from a given path.
"""

from os.path import join, expanduser, isfile, basename


def extract_filename_from_path(path: str) -> str:
    """
    Function to extract filename from given path.

    Arguments
    ---------
        path (str): File path

    Returns
    -------
        filename (str): File name from given `path`.
    """

    filename = ""

    if path.startswith("~"):
        path = join(expanduser("~"), path[2:])

    if isfile(path):
        # Method 1
        filename = path.split("/")[-1]

        # Method 2
        filename = basename(path)

    else:
        print("Not a file")

    return filename


if __name__ == "__main__":
    path = input()

    print(f"Filename = {extract_filename_from_path(path)}")
