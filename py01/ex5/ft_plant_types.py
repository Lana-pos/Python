"""
This function introduces Inheritance by defining different types of plants:
Flowers, Trees, and Vegetables,
each inheriting from a base Plant class and adding their own unique attributes
and methods.
"""


class Plant:
    """ Base class representing a plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes the Plant object with name, height, and age.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Class representing a flower, inheriting from Plant and adding color
    attribute.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes the Flower object with specific attributes."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Displays a blooming message for the flower."""
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """
    Class representing a tree, inheriting from Plant and adding trunk_diameter
      attribute.
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initializes the Tree object with specific attributes."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculates and displays the shade area provided by the tree."""
        shade_area = self.trunk_diameter * self.height * 3.14/1000
        print(f"{self.name} provides {shade_area:.0f}"
              f"square meters of shade.\n")


class Vegetable(Plant):
    """
    Class representing a vegetable, inheriting from Plant
    and adding harvest_season and nutritional_value attributes.
    """
    def __init__(self, name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initializes the Vegetable object with specific attributes.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self) -> None:
        """
        Displays information about the vegetable.
        """
        print(f"{self.name} is harvested in {self.harvest_season}"
              f"and is rich in {self.nutritional_value}.\n")


def ft_plant_types() -> None:
    """
    Demonstrates different plant types using inheritance.
    Creates instances of Flower, Tree, and Vegetable and
    displays their unique attributes and behaviors.
    """
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 30, 15, "white")
    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 1000, 7300, 40)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    pumpkin = Vegetable("Pumpkin", 50, 120, "autumn", "beta-carotene")

    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days"
          f" {rose.color} color")
    rose.bloom()
    print(f"{lily.name} (Flower): {lily.height}cm, {lily.age} days"
          f" {lily.color} color")
    lily.bloom()

    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days,"
          f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    print(f"{maple.name} (Tree): {maple.height}cm, {maple.age} days,"
          f"{maple.trunk_diameter}cm diameter")
    maple.produce_shade()

    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days,"
          f"{tomato.harvest_season} harvest")
    tomato.info()

    print(f"{pumpkin.name} (Vegetable): {pumpkin.height}cm, {pumpkin.age} days"
          f",{pumpkin.harvest_season} harvest")
    pumpkin.info()


if __name__ == "__main__":
    ft_plant_types()
