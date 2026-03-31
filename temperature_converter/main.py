
import logging
from haashi_pkg.utility import Logger, ScreenUtil as su
from typing import Optional, Union
    
def main(logger: Optional[Logger] = None) -> None:
    
    logger = logger or Logger(logging.INFO)

    while True:
        su.clear_screen()
        logger.info("Temp Converter")

        unit = validate_unit(input("Unit: "), logger)
        if unit is None continue else pass
        
        value = validate_value(input("Value: "), logger)
        if value is None continue else pass
        
        _unit = validate_unit(input("Convert to: "), logger)
        if _unit is None continue else pass



    
def validate_unit(unit: Optional[str] = None, logger: Optional[Logger] = None) -> Optional[str]:
    
    if not unit:
        logger.warning("Unit field cannot be empty!")
        su.wait_and_enter()
        return

    if unit not in ["c", "k", "f",]:
        logger.warning(f"Value: ({unit}) is invalid!")
        su.wait_and_enter()
        return

    return unit.lower().strip()


def validate_value(value: Optional[str] = None, logger: Optional[Logger] = None) -> Optional(Union[float, int]):

    if not value:
        logger.warning("Value field cannot be empty!")
        su.wait_and_enter()
        return

    try:
        if float(value).is_integer():
            return int(value)
        
        return float(value)

    except ValueError:
        logger.warning(f"Value: ({value}) is not a valid integer or float!")
        su.wait_and_enter()
        return

    


