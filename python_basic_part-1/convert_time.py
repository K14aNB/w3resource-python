"""
Task
----
Write a python program to convert all units of time.
"""


def convert_time(current: str = "min", to: str = "sec", time: float = 0.0) -> float:
    """
    Function to convert time from one unit to another unit.

    Arguments
    ---------
        current (str): Indicates the current unit in which time is given. Can take values like sec, seconds, min, minutes, hr, hours, days, months, years. Default = min
        to (str): Indicates the unit to which time is to be converted to. Can take values like sec, seconds, min, minutes, hr, hours, days, months, years. Default = sec
        time (float): Time in specific unit. Default = 0.0

    Returns
    -------
        converted_time (float): Time from `time` converted to the unit as per value of `to`.
    """

    converted_time = time

    if to != current and current in [
        "secs",
        "seconds",
        "mins",
        "minutes",
        "hrs",
        "hours",
        "days",
        "months",
        "years",
    ]:
        match to.lower():
            case "secs" | "seconds":
                if current in ["mins", "minutes"]:
                    converted_time *= 60
                elif current in ["hrs", "hours"]:
                    converted_time *= 3600
                elif current == "days":
                    converted_time *= 86400
                elif current == "months":
                    converted_time *= 2629746
                elif current == "years":
                    converted_time *= 31556952

            case "mins" | "minutes":
                if current in ["secs", "seconds"]:
                    converted_time /= 60
                elif current in ["hrs", "hours"]:
                    converted_time *= 60
                elif current == "days":
                    converted_time *= 1440
                elif current == "months":
                    converted_time *= 43800
                elif current == "years":
                    converted_time *= 525600

            case "hrs" | "hours":
                if current in ["secs", "seconds"]:
                    converted_time /= 3600
                elif current in ["mins", "minutes"]:
                    converted_time /= 60
                elif current == "days":
                    converted_time *= 24
                elif current == "months":
                    converted_time *= 730.001
                elif current == "years":
                    converted_time *= 8760

            case "days":
                if current in ["secs", "seconds"]:
                    converted_time /= 86400
                elif current in ["mins", "minutes"]:
                    converted_time /= 1440
                elif current in ["hrs", "hours"]:
                    converted_time /= 24
                elif current == "months":
                    converted_time *= 30
                elif current == "years":
                    converted_time *= 365

            case "months":
                if current in ["secs", "seconds"]:
                    converted_time /= 2629746
                elif current in ["mins", "minutes"]:
                    converted_time /= 43800
                elif current in ["hrs", "hours"]:
                    converted_time /= 730.001
                elif current == "days":
                    converted_time /= 30
                elif current == "years":
                    converted_time *= 12

            case "years":
                if current in ["secs", "seconds"]:
                    converted_time /= 31556952
                elif current in ["mins", "minutes"]:
                    converted_time /= 525600
                elif current in ["hrs", "hours"]:
                    converted_time /= 8760
                elif current == "days":
                    converted_time /= 365
                elif current == "months":
                    converted_time /= 12

            case _:
                print("Invalid Units")
    else:
        print("Please enter time in valid units")

    if converted_time != time:
        return converted_time


if __name__ == "__main__":
    time = float(input("Enter time:"))
    current = input("Enter current unit:")
    to = input("Enter unit to be converted to:")

    print(f"Time in {to} = {convert_time(current, to, time)}")
