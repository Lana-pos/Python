"""
This module defines custom exceptions for garden-related errors
and demonstrates their usage in various scenarios.
"""


class GardenError(Exception):
    """
    Base class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for plant-related errors.
    """
    pass


class WaterError(GardenError):
    """
    Exception raised for water-related errors.
    """
    pass


def health_checker(is_not_healthy: bool):
    """
    Check the health of a plant.
    If the plant is not healthy, raise a PlantError.
    """
    if is_not_healthy:
        raise PlantError("The tomato plant is wilting!")


def water_checker(liters):
    """
    Check the water level in the tank.
    If the water level is below 5 liters, raise a WaterError.
    """
    if liters < 5:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """
    Test the custom garden error classes.
    1. Test PlantError by simulating an unhealthy plant.
    2. Test WaterError by simulating low water level.
    3. Test catching all garden errors using the base class GardenError.
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        health_checker(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_checker(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    try:
        health_checker(True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        water_checker(3)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
