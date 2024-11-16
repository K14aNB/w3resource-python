"""
Task
----
Write a python program to create a copy of it's own source code.
"""

from os.path import isfile
from shutil import copyfile


def copy_file(src: str, dest: str) -> None:
    """
    Function to copy a file from source to destination.

    Arguments
    ---------
        src (str): Source file path
        dest (str): Destination file path

    Returns
    -------
        None
    """

    if isfile(src) and isfile(dest):
        copyfile(src, dest)


if __name__ == "__main__":
    src = input("Enter path of file to be copied:")
    dest = input("Enter destination directory:")

    copy_file(src, dest)
