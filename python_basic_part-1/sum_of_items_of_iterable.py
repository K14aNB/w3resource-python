"""
Task
----
Write a python program to calculate the sum of all items of a container (tuple, set, list, dictionary).
"""

import builtins


def sum_of_items(
    container: list[int | float | bool]
    | tuple[int | float | bool]
    | set[int | float | bool]
    | dict[str, int | float | bool],
) -> float:
    """
    Function to calculate the sum of items in a container.

    Arguments
    ---------
        container (list[int | float | bool] | tuple[int | float | bool] | set[int | float | bool] | dict[str, int | float | bool]): An iterable containing items.

    Returns
    -------
        sum (float): Sum of items in the `container`
    """

    sum_of_items: float = 0.0

    if len(container) > 0 and type(container) in [list, tuple, set]:
        for item in container:
            sum_of_items += item  # type: ignore

    elif len(container) > 0 and isinstance(container, dict):
        for value in container.values():
            sum_of_items += value

    return sum_of_items  # type: ignore


if __name__ == "__main__":
    valid_data_types: int = 0
    container_type = input("Enter type of iterable:")
    data_types = input("Enter data types:").split(",")
    for dt in data_types:
        if dt in ["int", "float", "bool"]:
            valid_data_types += 1

    if container_type in ["list", "tuple", "set", "dict"] and valid_data_types == len(
        data_types
    ):
        match container_type.lower():
            case "list":
                container: list[int | float | bool] = []  # type: ignore
                for dt1 in data_types:
                    container.append(  # type: ignore
                        getattr(builtins, dt1)(  # type: ignore
                            input(f"Enter {dt1} data:")
                        )
                    )

            case "tuple":
                temp_list: list[int | float | bool] = []
                for dt2 in data_types:
                    temp_list.append(
                        getattr(builtins, dt2)(  # type: ignore
                            input(f"Enter {dt2} data:")
                        )
                    )
                container = tuple(temp_list)  # type: ignore

            case "set":
                container: set[int | float | bool] = set()  # type: ignore
                for dt3 in data_types:
                    container.add(  # type: ignore
                        getattr(builtins, dt3)(  # type: ignore
                            input(f"Enter {dt3} data:")
                        )
                    )

            case "dict":
                container: dict[str, int | float | bool] = {}
                for ind, dt4 in enumerate(data_types):
                    container[ind] = getattr(builtins, dt4)(  # type: ignore
                        input(f"Enter {dt4} data:")
                    )

            case _:
                pass

        print(f"Sum of items = {sum_of_items(container)}")  # type: ignore
