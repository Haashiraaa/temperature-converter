

# temperature_conversions.py

from temperature_converter.aliases import ValueLike


class TemperatureConverter:
    """
    Handles temperature conversions between units.
    Provides clear methods for each conversion path.
    """

    KELVIN_OFFSET = 273.15

    @classmethod
    def kelvin_to_celsius(cls, value: ValueLike) -> float:
        """Convert Kelvin to Celsius."""
        return value - cls.KELVIN_OFFSET

    @classmethod
    def kelvin_to_fahrenheit(cls, value: ValueLike) -> float:
        """Convert Kelvin to Fahrenheit."""
        return (value - cls.KELVIN_OFFSET) * 9 / 5 + 32

    @classmethod
    def celsius_to_kelvin(cls, value: ValueLike) -> float:
        """Convert Celsius to Kelvin."""
        return value + cls.KELVIN_OFFSET

    @classmethod
    def celsius_to_fahrenheit(cls, value: ValueLike) -> float:
        """Convert Celsius to Fahrenheit."""
        return value * 9 / 5 + 32

    @classmethod
    def fahrenheit_to_kelvin(cls, value: ValueLike) -> float:
        """Convert Fahrenheit to Kelvin."""
        return (value - 32) * 5 / 9 + cls.KELVIN_OFFSET

    @classmethod
    def fahrenheit_to_celsius(cls, value: ValueLike) -> float:
        """Convert Fahrenheit to Celsius."""
        return (value - 32) * 5 / 9
