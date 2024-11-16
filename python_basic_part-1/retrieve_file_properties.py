"""
Task
----
Write a python program to retrieve file properties.
"""

from os.path import getatime, getctime, getmtime, getsize, expanduser, join, isfile
from time import ctime


def get_file_properties(file_path: str) -> tuple[str]:
    """
    Function to retrieve file properties.

    Arguments
    ---------
        file_path (str): path of the file for which properties are to be retrieved.

    Returns
    -------
        file_properties (tuple[str]): File properties of the file of given `file_path`.
    """

    if file_path.startswith("~"):
        file_path = join(expanduser("~"), file_path[2:])

    if isfile(file_path):
        return (
            getsize(file_path),
            ctime(getctime(file_path)),
            ctime(getmtime(file_path)),
            ctime(getatime(file_path)),
        )


if __name__ == "__main__":
    file_path = input("Enter file path:")

    file_props = get_file_properties(file_path)

    if len(file_props) > 0:
        print(f"File Properties of {file_path}")
        print(f"File size = {file_props[0]}")
        print(f"File creation time = {file_props[1]}")
        print(f"File modification time = {file_props[2]}")
        print(f"File access time = {file_props[3]}")
