"""
This module demonstrates the use of finally blocks in Python.
It simulates a garden watering system and shows how finally blocks
ensure cleanup code runs regardless of exceptions.
"""


def water_plants(plant_list):
    """
    Simulate watering a list of plants.
    Uses a finally block to ensure the watering system is closed
    regardless of whether an error occurs.
    """
    print("Opening watering system")
    try:
        for i in plant_list:
            if i is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {i}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the garden watering system with and without errors.
    """
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    good_plant_list = (["tomato", "lettuce", "carrots"])
    water_plants(good_plant_list)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    bad_plant_list = (["tomato", None])
    water_plants(bad_plant_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
