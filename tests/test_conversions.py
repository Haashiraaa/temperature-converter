

import pytest
from temperature_converter.conversions import TemperatureConverter
from tests.aliases import SampleValueLike


@pytest.fixture
def kelvin_offset() -> float:
    return 273.15


@pytest.fixture
def sample_values() -> SampleValueLike:
    return [
        (5, None),
        (94.2, None),
        (-56.8, None),
        ("invalid", TypeError),
        (None, TypeError),

    ]


def test_kelvin_to_celsuis(
    sample_values: SampleValueLike,
    kelvin_offset: float,
) -> None:

    for value, error in sample_values:

        if error is not None:
            with pytest.raises(error):
                TemperatureConverter.kelvin_to_celsius(
                    value)  # type: ignore[arg-type]
        else:

            result = TemperatureConverter.kelvin_to_celsius(
                value)  # type: ignore[arg-type]
            expected = value - kelvin_offset  # type: ignore[arg-type]

            assert result == expected


def test_kelvin_to_fahrenheit(
    sample_values: SampleValueLike,
    kelvin_offset: float,
) -> None:

    for value, error in sample_values:

        if error is not None:
            with pytest.raises(error):
                TemperatureConverter.kelvin_to_fahrenheit(
                    value)  # type: ignore[arg-type]
        else:

            result = TemperatureConverter.kelvin_to_fahrenheit(
                value)  # type: ignore[arg-type]
            expected = (  # type: ignore[arg-type]
                value - kelvin_offset
            ) * 9 / 5 + 32
            assert result == expected


def test_celsius_to_kelvin(
    sample_values: SampleValueLike,
    kelvin_offset: float,
) -> None:

    for value, error in sample_values:

        if error is not None:
            with pytest.raises(error):
                TemperatureConverter.celsius_to_kelvin(
                    value)  # type: ignore[arg-type]
        else:

            result = TemperatureConverter.celsius_to_kelvin(
                value)  # type: ignore[arg-type]
            expected = value + kelvin_offset  # type: ignore[arg-type]

            assert result == expected


def test_celsius_to_fahrenheit(sample_values: SampleValueLike) -> None:

    for value, error in sample_values:

        if error is not None:
            with pytest.raises(error):
                TemperatureConverter.celsius_to_fahrenheit(
                    value)  # type: ignore[arg-type]
        else:

            result = TemperatureConverter.celsius_to_fahrenheit(
                value)  # type: ignore[arg-type]
            expected = value * 9 / 5 + 32  # type: ignore[arg-type]

            assert result == expected


def test_fahrenheit_to_kelvin(
    sample_values: SampleValueLike,
    kelvin_offset: float,
) -> None:

    for value, error in sample_values:

        if error is not None:
            with pytest.raises(error):
                TemperatureConverter.fahrenheit_to_kelvin(
                    value)  # type: ignore[arg-type]
        else:

            result = TemperatureConverter.fahrenheit_to_kelvin(
                value)  # type: ignore[arg-type]
            expected = (  # type: ignore[arg-type]
                value - 32) * 5 / 9 + kelvin_offset

            assert result == expected


def test_fahrenheit_to_celsius(sample_values: SampleValueLike,) -> None:

    for value, error in sample_values:

        if error is not None:
            with pytest.raises(error):
                TemperatureConverter.fahrenheit_to_celsius(
                    value)  # type: ignore[arg-type]
        else:

            result = TemperatureConverter.fahrenheit_to_celsius(
                value)  # type: ignore[arg-type]
            expected = (  # type: ignore[arg-type]
                value - 32) * 5 / 9

            assert result == expected
