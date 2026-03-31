# temperature-converter

A CLI tool for converting temperatures between Celsius, Kelvin, and Fahrenheit.


---

## Project Structure

```
temperature-converter/
├── temperature_converter/
│   ├── __init__.py
│   ├── main.py          # Entry point and main loop
│   ├── conversions.py   # Conversion logic
│   ├── validations.py   # Input validation and routing
│   ├── guide.py         # User guide display
│   └── aliases.py       # Shared type aliases
└── requirements.txt
```

---

## Dependencies

- Python 3.10+
- [`haashi_pkg`](https://github.com/Haashiraaa/haashi-analytics-toolkit) — used for logging (`Logger`) and screen utilities (`ScreenUtil`)

---

## Installation

```bash
git clone https://github.com/Haashiraaa/temperature-converter.git
cd temperature-converter
pip install -r requirements.txt
```

---

## Usage

```bash
python -m temperature_converter.main
```

Or directly:

```bash
python temperature_converter/main.py
```

On launch you will be asked if you want to view the guide. After that the main loop runs:

```
Unit: c
Value: 100
Convert to: f

Result = 212.0°F
```

Enter `q` at any prompt to exit. `Ctrl+C` also exits cleanly.

---

## Modules

### `aliases.py`

- `ValueLike = Union[int, float]`

---

### `conversions.py`

`TemperatureConverter` — all methods are `@classmethod`. Uses `KELVIN_OFFSET = 273.15`.

| Method | Formula |
|---|---|
| `celsius_to_fahrenheit` | `v * 9/5 + 32` |
| `celsius_to_kelvin` | `v + 273.15` |
| `fahrenheit_to_celsius` | `(v - 32) * 5/9` |
| `fahrenheit_to_kelvin` | `(v - 32) * 5/9 + 273.15` |
| `kelvin_to_celsius` | `v - 273.15` |
| `kelvin_to_fahrenheit` | `(v - 273.15) * 9/5 + 32` |

---

### `validations.py`

- `validate_unit(unit, logger)` — Accepts `k`, `c`, or `f`. Returns `None` on empty or invalid input, exits on `q`
- `validate_value(value, logger)` — Parses to `int` or `float`. Returns `None` on empty or non-numeric input, exits on `q`
- `validate_route(unit, _unit, logger)` — Looks up the conversion function from the `routes` dict. Returns `None` if the pair is unsupported
- `validate_guide_response(response, logger)` — Returns `True` for `y`/`yes`, `False` for `n`/`no`/empty, `None` otherwise

The `routes` dict maps `(from_unit, to_unit)` tuples directly to `TemperatureConverter` methods, covering all 6 conversion paths.

---

### `guide.py`

`guide()` — prints a formatted usage guide to stdout showing accepted unit symbols and commands.

---

### `main.py`

- Prompts the user to optionally view the guide on startup
- Runs a `while True` loop collecting unit, value, and target unit in sequence
- Dispatches to the correct conversion function via `validate_route`
- Handles `KeyboardInterrupt` cleanly and logs unhandled exceptions to JSON before exiting

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| Empty input | Warning logged, loop restarts |
| Invalid unit | Warning logged, loop restarts |
| Non-numeric value | Warning logged, loop restarts |
| `q` entered | Clean exit |
| `KeyboardInterrupt` | Clean exit with message |
| Unhandled exception | Error logged to JSON, `sys.exit(1)` |

---

## Author

Haashiraaa
