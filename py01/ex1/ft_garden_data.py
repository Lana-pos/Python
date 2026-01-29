"""A simple program that prints information about plants in a garden."""


class Plant:
    """Class representing a plant in a garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the Plant object with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def info(self) -> None:
        """Prints the plant's information in a formatted string."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    """Main function to create and display plant information."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.info()
    sunflower.info()
    cactus.info()


if __name__ == "__main__":
    main()
