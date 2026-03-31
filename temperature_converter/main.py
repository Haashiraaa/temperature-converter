

# temperature_converter/main.py

import logging
import sys
from typing import Optional, Dict
from haashi_pkg.utility import Logger, ScreenUtil as su
from temperature_converter.validations import (
    validate_unit, validate_value, validate_route, validate_guide_response
)
from temperature_converter.guide import guide

unit_symbols: Dict[str, str] = {"k": "K", "c": "°C", "f": "°F"}


def main(logger: Optional[Logger] = None) -> None:

    logger = logger or Logger(logging.INFO)

    su.space()
    logger.info("Hello! Welcome to the Temperature Converter!")
    logger.info("This program will help you with temperature conversions.")
    su.space()

    logger.info("Would you like to see the guide? (y/n)")
    view_guide = validate_guide_response(input(">>> "))

    if view_guide is True:
        su.space()
        guide()
        su.space()

    su.wait_and_enter()

    while True:
        su.clear_screen()
        su.space()
        logger.info("Temp Converter")
        su.space()

        try:
            unit = validate_unit(input("Unit: "), logger)
            if unit is None:
                continue

            value = validate_value(input("Value: "), logger)
            if value is None:
                continue

            _unit = validate_unit(input("Convert to: "), logger)
            if _unit is None:
                continue

            func = validate_route(unit, _unit, logger)
            if func is None:
                continue

            converted_value = func(value)

            su.space()
            logger.info(f"Result = {converted_value}{unit_symbols[_unit]}")
            su.wait_and_enter()

        except KeyboardInterrupt:
            su.space()
            logger.info("Program interrupted!")
            sys.exit(0)

        except Exception as e:
            su.space()
            logger.error(f"Error: {e}")
            logger.error(exception=e, save_to_json=True)
            sys.exit(1)


if __name__ == "__main__":
    main()
