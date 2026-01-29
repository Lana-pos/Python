"""
Garden Management System
This module defines classes to manage a garden with various types of plants,
including flowering plants and prize-winning flowers. It includes functionality
to grow plants, generate reports, and calculate garden statistics.
"""


class Plant:
    """
    Base class representing a plant in the garden. Includes basic attributes
    and methods for growth.
    """

    def __init__(self, name: str, height: int) -> None:
        """
        Initializes the Plant object with name and height.
        """
        self.name = name
        self.height = height

    def grow_plant(self, cm: int) -> None:
        """
        Increases the height of the plant by the specified centimeters.
        """
        self.height = self.height + cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    """
    Class representing a flowering plant, inheriting from Plant and adding
    color attribute."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialize a flowering plant with basic plant attributes and color.
        """
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """
    A high-quality flowering plant that carries competitive prize points.
    Inherits from FloweringPlant.
    """

    def __init__(self, name: str, height: int, color: str, points: int):
        """
        Initializes a PrizeFlower with name, height, color, and prize points.
        """
        super().__init__(name, height, color)
        self.points = points

    def __str__(self) -> str:
        """
        Returns a string representation of the PrizeFlower.
        """
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")


class GardenManager:
    """
    Main controller class for managing a garden, its plants, statistics, and
    reports.
    """

    collection_of_gardens = 0

    class GardenStats:
        """
        Nested helper class for calculating garden statistics.
        """

        def score(self, plants: list[any]) -> int:
            """
            Calculates the total score of the garden based on plant heights
            and prize points.
            """
            score = 0
            for p in plants:
                score += p.height
                if hasattr(p, 'points'):
                    score += p.points * 10
            return score

    def __init__(self, owner: str) -> None:
        """
        Setup a new garden manager for a specific owner.
        """
        self.owner = owner
        self.plants: list[any] = []
        self.stats = self.GardenStats()
        GardenManager.collection_of_gardens += 1

    def add_plant(self, plant) -> None:
        """
        Adds a plant to the garden's collection.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_everything(self) -> None:
        """
        Increment the height of every plant in the garden by 1cm.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow_plant(1)

    def generate_report(self) -> None:
        """
        Display a detailed status report for plants and the total garden score.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                print(p)
            elif isinstance(p, FloweringPlant):
                print(f"{p.name}: {p.height}cm, {p.color} flowers (blooming)")
            else:
                print(f"{p.name}: {p.height}cm")

        print(f"Plants added: {len(self.plants)}")

        score = self.stats.score(self.plants)
        print(f"Garden score for {self.owner}: {score}")

    @classmethod
    def garden_creation(cls, owners: list[str]) -> list['GardenManager']:
        """
        Class method to create multiple GardenManager instances for given
        owners."""
        return [cls(owner) for owner in owners]

    @staticmethod
    def height_validation(height: int) -> bool:
        """
        Static method to validate if a plant's height is non-negative.
        """
        return height >= 0


def main() -> None:
    """
    Main execution entry point to demonstrate the garden management system.
    """
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")

    pl1 = Plant("Oak Tree", 100)
    pl2 = FloweringPlant("Rose", 25, "red")
    pl3 = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(pl1)
    alice.add_plant(pl2)
    alice.add_plant(pl3)

    alice.grow_everything()
    alice.generate_report()

    print(f"Height validation test: {GardenManager.height_validation(10)}")

    bob = GardenManager("Bob")
    bob.add_plant(Plant("Bush", 90))
    bob_score = bob.stats.score(bob.plants)

    print(f"Garden scores of Alice: {alice.stats.score(alice.plants)}, "
          f"Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.collection_of_gardens}")


if __name__ == "__main__":
    main()
