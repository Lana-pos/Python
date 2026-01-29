"""A plant factory that creates multiple plant
instances and displays their information."""


class Plant:
    """Class representing a plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Class representing a plant."""
        self.name = name
        self.height = height
        self.age = age


def factory() -> None:
    """Creates multiple plant instances and displays their information."""

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    factory()
