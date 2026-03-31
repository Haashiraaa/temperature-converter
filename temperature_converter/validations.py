

# temperature_converter/validations.py

import logging
import sys
from haashi_pkg.utility import Logger, ScreenUtil as su
from temperature_converter.conversions import TemperatureConverter
from temperature_converter.aliases import ValueLike
from typing import Optional, Union, Dict, Tuple, Callable


routes: Dict[Tuple[str, str], Callable[[ValueLike], float]] = {
    ("k", "c"): TemperatureConverter.kelvin_to_celsius,
    ("k", "f"): TemperatureConverter.kelvin_to_fahrenheit,
    ("c", "k"): TemperatureConverter.celsius_to_kelvin,
    ("c", "f"): TemperatureConverter.celsius_to_fahrenheit,
    ("f", "k"): TemperatureConverter.fahrenheit_to_kelvin,
    ("f", "c"): TemperatureConverter.fahrenheit_to_celsius,
}


def validate_unit(unit: Optional[str] = None, logger: Optional[Logger] = None) -> Optional[str]:

    logger = logger or Logger(logging.INFO)
    unit = unit.lower().strip() if unit is not None else None

    if not unit:
        su.space()
        logger.warning("Unit field cannot be empty!")
        su.wait_and_enter()
        return

    if unit == "q":
        su.space()
        logger.info("Exiting Program...")
        sys.exit(0)

    if unit not in ["c", "k", "f",]:
        su.space()
        logger.warning(f"Unit: ({unit}) is invalid!")
        su.wait_and_enter()
        return

    return unit


def validate_value(
    value: Optional[str] = None,
    logger: Optional[Logger] = None
) -> Optional[Union[float, int]]:

    logger = logger or Logger(logging.INFO)
    value = value.lower().strip() if value is not None else None

    if not value:
        su.space()
        logger.warning("Value field cannot be empty!")
        su.wait_and_enter()
        return

    if value == "q":
        su.space()
        logger.info("Exiting Program...")
        sys.exit(0)

    try:
        if float(value).is_integer():
            return int(value)

        return float(value)

    except ValueError:
        su.space()
        logger.warning(f"Value: ({value}) is not a valid integer or float!")
        su.wait_and_enter()
        return


def validate_route(
    unit: str, _unit: str, logger: Optional[Logger] = None
) -> Optional[Callable[[ValueLike], float]]:

    logger = logger or Logger(logging.INFO)

    func = routes.get((unit, _unit))
    if not func:
        su.space()
        logger.warning("Unsupported conversion!")
        su.wait_and_enter()
        return

    return func


def validate_guide_response(
    response: str, logger: Optional[Logger] = None
) -> Optional[bool]:

    logger = logger or Logger(logging.INFO)

    valid_responses = ["y", "yes", "n", "no", ""]

    if response in ["y", "yes"]:
        return True

    if response in ["n", "no", ""]:
        return False

    if response not in valid_responses:
        return
