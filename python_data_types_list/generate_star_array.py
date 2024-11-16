"""
Task
----
Write a python program to generate a 3*4*6 3D array whose each element is '*'.
"""

import numpy as np
from numpy.typing import NDArray

# Method 1
star_list = ["*" for _ in range(72)]
star_array: NDArray[np.str_] = np.array(star_list, ndmin=3).reshape(3, 4, 6)

print(star_array)

# Method 2

star_arr: list[list[list[str]]] = [
    [["*" for _ in range(6)] for _ in range(4)] for _ in range(3)
]
