"""
This module checks if the provided temperature is within the acceptable range
for plants.
If the temperature is invalid, it prints an error message instead of raising
an exception.
"""


def check_temperature(temp: str) -> int | None:
    """
    Check if the temperature is within the acceptable range for plants.
    """
    try:
        temp = int(temp)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
    except ValueError:
        print(f"Error: '{temp}' is not a valid number")
        return None


def test_temperature_input():
    """
    Test various temperature inputs to check error handling.
    """
    print("=== Garden Temperature Checker ===")
    connections = [
        "25",
        "abc",
        "100",
        "-50"
        ]

    for i in connections:
        print(f"Testing temperature: {i}")
        check_temperature(i)
        print('\n')


if __name__ == "__main__":
    test_temperature_input()
