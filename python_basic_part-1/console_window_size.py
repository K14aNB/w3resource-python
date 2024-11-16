"""
Task
----
Write a python program to get the height and width of the console window.
"""

from fcntl import ioctl
from termios import TIOCGWINSZ
from struct import pack, unpack


def get_terminal_size() -> tuple[int]:
    """
    Function to return the size of console window.

    Arguments
    ---------
        None

    Returns
    -------
        terminal_size (tuple[int]): Returns width, height of the console window as a tuple.
    """

    th, tw, hp, wp = unpack("HHHH", ioctl(0, TIOCGWINSZ, pack("HHHH", 0, 0, 0, 0)))

    return tw, th


if __name__ == "__main__":
    print(f"Console Window size : {get_terminal_size()}")
