"""
Task
----
Write a python program to get a directory listing, sorted by creation date.
"""

from os.path import getctime, isfile, join, expanduser
from os import listdir


def directory_listing_by_creation_time(path: str) -> list[str]:
    """
    Function to get directory listing with files sorted by creation time.

    Arguments
    ---------
        path (str): Absolute path of the directory.

    Returns
    -------
        listing_by_creation_time (list[str]): List of files in the directory given by `path`
    """

    if path.startswith("~"):
        path = path.replace("~", expanduser("~"))
    list_dirs = [join(path, file) for file in listdir(path) if isfile(join(path, file))]
    list_dirs.sort(key=getctime)

    return list_dirs


if __name__ == "__main__":
    dir_path = input(
        "Enter absolute path of the directory to get a listing sorted by creation time:"
    )

    print(f"Directory listing for {dir_path}, sorted by creation time = {
          directory_listing_by_creation_time(dir_path)}")
