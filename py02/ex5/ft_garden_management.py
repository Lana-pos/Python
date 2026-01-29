"""
This module provides a GardenManager class to manage garden plants. It includes
custom exceptions for garden-related errors and demonstrates their usage in
various scenarios such as adding plants, watering them, and checking
their health.
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


class GardenManager:
    """
    A class to manage garden plants, including adding plants, watering them,
    and checking their health.
    """
    def __init__(self):
        """
        Initialize the GardenManager with an empty list of plants.
        """
        self.plants = []

    def add_plant(self, name: str):
        """
        Add a plant to the garden.
        Raises ValueError if the plant name is empty.
        """
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plant(self):
        """
        Water all plants in the garden.
        Uses a finally block to ensure the watering system is closed
        regardless of whether an error occurs.
        """
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for i in self.plants:
                print(f"Watering {i} - success")
        except WaterError as e:
            print(f"Watering error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water: int, sun: int):
        """
        Check if the plant is healthy based on water level and sunlight hours.
        Raises PlantError with descriptive messages if any parameter is out of
        range.
        """
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise PlantError(f"Sunlight {sun} is too low (min 2)")
        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """
    Test the GardenManager class and custom exceptions.
    1. Add plants to the garden.
    2. Water the plants.
    3. Check plant health with valid and invalid parameters.
    4. Demonstrate error recovery from a GardenError.
    5. Print completion message.
    """
    manager = GardenManager()
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except ValueError as e:
        print(f"Error adding plant: {e}")
    manager.water_plant()
    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    try:
        manager.check_plant_health("lettuce", 15, 8)
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
