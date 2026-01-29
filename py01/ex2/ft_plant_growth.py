"""A program that prints information about plants,
it simulates time passing and calculates how much things changed."""


class Plant:
    """Class representing a plant in a garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the Plant object with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Simulates the growth of the plant by increasing its height."""
        self.height = self.height + 1

    def age_up(self) -> None:
        """Increases the age of the plant by one day."""
        self.age = self.age + 1

    def get_info(self) -> None:
        """Prints the plant's information in a formatted string."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth():
    """Main function to create and display plant information."""

    flowers = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    originals = []
    for p in flowers:
        originals.append({"h": p.height, "a": p.age})

    print("=== Day 1 ===")
    for p in flowers:
        p.get_info()

    for _ in range(6):
        for p in flowers:
            p.grow()
            p.age_up()

    print("\n=== Day 7 ===")
    for i in range(len(flowers)):
        flowers[i].get_info()

        growth = flowers[i].height - originals[i]["h"]
        aging = flowers[i].age - originals[i]["a"]

        print(f"  > Growth: +{growth}cm, +{aging} days\n")


if __name__ == "__main__":
    ft_plant_growth()
