"""
Task
----
Write python program to convert pressure from one unit to another unit.
"""

# TO DO


def convert_pressure(
    current: str = "pa", to: str = "atm", pressure: float = 101325.0
) -> float:
    """
    Function to convert pressure from one unit to another unit.

    Arguments
    ---------
        current (str): Indicates current unit in which pressure is given. Can take values like pa, atm, cm_of_H2O, cm_of_Hg, ft_of_H2O_column, kgf_per_sq_cm, hectopa, in_of_H2O_column, in_of_Hg, torr, bar, kgf_per_sq_m, kn_per_sq_m, millibar, m_of_H2O_column, m_of_Hg, mm_of_H2O_column, mm_of_Hg, megapa, oz_force_per_sq_in, lb_per_sq_in. Default = pa
        to (str): Indicates the unit to which pressure is to be converted into. Can take values like pa, atm, cm_of_H2O, cm_of_Hg, ft_of_H2O_column, kgf_per_sq_cm, hectopa, in_of_H2O_column, in_of_Hg, torr, bar, kgf_per_sq_m, kn_per_sq_m, millibar, m_of_H2O_column, m_of_Hg, mm_of_H2O_column, mm_of_Hg, megapa, oz_force_per_sq_in, lb_per_sq_in. Default = atm
        pressure (float): Pressure in specific unit. Default = 101325.0

    Returns
    -------
        converted_pressure (float): Pressure from `pressure` converted to unit as per value of `to`.
    """

    converted_pressure = pressure

    if to != current and current in [
        "pa",
        "atm",
        "cm_of_H2O",
        "cm_of_Hg",
        "ft_of_H2O_column",
        "kgf_per_sq_cm",
        "hectopa",
        "in_of_H2O_column",
        "in_of_Hg",
        "torr",
        "bar",
        "kgf_per_sq_m",
        "kn_per_sq_m",
        "millibar",
        "m_of_H2O_column",
        "m_of_Hg",
        "mm_of_H2O_column",
        "mm_of_Hg",
        "megapa",
        "oz_force_per_sq_in",
        "lb_per_sq_in",
    ]:
        match to.lower():
            case "pa":
                match current.lower():
                    case "atm":
                        converted_pressure *= 101325

                    case "cm_of_H2O":
                        converted_pressure *= 98.0665

                    case "cm_of_Hg":
                        converted_pressure *= 1333.2239

                    case "ft_of_H2O_column":
                        converted_pressure *= 2988.98

                    case "kgf_per_sq_cm":
                        converted_pressure *= 98066.5

                    case "hectopa":
                        converted_pressure *= 100

                    case "in_of_H2O_column":
                        converted_pressure *= 248.84

                    case "in_of_Hg":
                        converted_pressure *= 3386.39

                    case "torr":
                        converted_pressure *= 133.322

                    case "bar":
                        converted_pressure *= 100000

                    case "kgf_per_sq_m":
                        converted_pressure *= 9.80665

                    case "kn_per_sq_m":
                        converted_pressure *= 0.001

                    case "millbar":
                        converted_pressure *= 100

                    case "m_of_H2O_column":
                        converted_pressure *= 9806.38

                    case "m_of_Hg":
                        converted_pressure *= 133322.4

                    case "mm_of_H2O_column":
                        converted_pressure *= 9.80638

                    case "mm_of_Hg":
                        converted_pressure *= 133.322

                    case "megapa":
                        converted_pressure *= 1000000

                    case "oz_force_per_sq_in":
                        converted_pressure *= 430.922

                    case "lb_per_sq_in":
                        converted_pressure *= 6894.76

            case "atm":
                match current.lower():
                    case "pa":
                        converted_pressure /= 101325

                    case "cm_of_H2O":
                        converted_pressure /= 1033

                    case "cm_of_Hg":
                        converted_pressure
