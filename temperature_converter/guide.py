
# guide.py


def guide() -> None:
    """Displays a quick usage guide for users."""
    guide = """
========================================
   TEMPERATURE CONVERTER — USER GUIDE
========================================
Steps:
  1) Choose a unit:
       k → Kelvin
       c → Celsius
       f → Fahrenheit

  2) Enter the temperature value.
  3) Choose the unit to convert to.

Commands:
  q → Quit anytime
========================================
"""
    print(guide)
