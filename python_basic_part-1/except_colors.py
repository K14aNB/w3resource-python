"""
Task
----
Write a python program that prints out all colors from color_list_1 that are not present in color_list_2.

Sample Input:
color_list_1 = set(['White', 'Black', 'Red'])
color_list_2 = set(['Red', 'Green'])

Output:
{'Black', 'White'}
"""


def except_colors_set(color_list_1: set[str], color_list_2: set[str]) -> set[str]:
    """
    Function to return the set of colors from color_list_1 that are not present in color_list_2

    Arguments
    ---------
        color_list_1 (set[str]): Set of colors
        color_list_2 (set[str]): Set of colors

    Returns
    -------
        except_set (set[str]): Set of colors from color_list_1 that are not present in color_list_2
    """

    except_set = set()

    for color in color_list_1:
        if color not in color_list_2:
            except_set.add(color)

    return except_set


if __name__ == "__main__":
    color_set_1 = set(map(str, input().split(",")))
    color_set_2 = set(map(str, input().split(",")))

    print(
        f"Colors from set 1 that are not present in set 2 = {
            except_colors_set(color_set_1, color_set_2)}"
    )
