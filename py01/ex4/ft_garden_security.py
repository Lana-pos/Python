"""Functionality: Implementation of a garden security system that
prevents negative values for plant attributes."""


class SecurePlant:
    """Class representing a plant with security checks on its attributes."""
    def __init__(self, name: str) -> None:
        """
        Initializes the SecurePlant object.
        """
        self.name = name
        self._height = 0
        self._age = 0

    def set_height(self, new_height: int) -> None:
        """
        Sets the height of the plant with security check.
        """
        if new_height < 0:
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """
        Sets the age of the plant with security check.
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age "
                  f"{new_age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_height(self) -> int:
        """
        returns the height of the plant.
        """
        return self._height

    def get_age(self) -> int:
        """
        returns the age of the plant.
        """
        return self._age

    def display(self) -> None:
        """
        Displays the current state of the plant.
        """
        print(f"Current plant: {self.name} ({self._height}cm, "
              f"{self._age} days)")


def ft_garden_security() -> None:
    """
    Demonstrates the garden security system by creating a SecurePlant instance
    and attempting to set its attributes with both valid and invalid values.
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.display()


if __name__ == "__main__":
    ft_garden_security()
