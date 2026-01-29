"""A simple program that prints information about a plant in a garden."""


def ft_garden_plant() -> None:
    """Prints information about a plant in the garden."""
    name: str = "Plant: Rose"
    height: int = 25
    age: int = 30

    print(f"{name}\nHeight: {height}cm\nAge: {age}days")


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    ft_garden_plant()
    print("\n=== End of Program ===")
