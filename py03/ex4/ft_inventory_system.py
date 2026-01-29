"""
A module that implements an inventory system for a game.
It processes command-line arguments to build an inventory and provides
"""


import sys
"""
sys module is used to handle command-line arguments
"""


def inventory_system():
    """
    Main function to process inventory data from command-line arguments.
    Analyzes the inventory and provides statistics and management suggestions.
    1. Parses item:count pairs from command-line arguments.
    2. Calculates total items and unique item types.
    3. Displays current inventory with percentages.
    4. Identifies most and least abundant items.
    5. Categorizes items into 'Moderate' and 'Scarce'.
    6. Suggests items that need restocking.
    7. Demonstrates dictionary properties and sample lookups.
    """
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} item:count ...")
        return

    print("=== Inventory System Analysis ===")

    inventory = {}

    for i in sys.argv[1:]:
        if ":" in i:
            name, count_str = i.split(":")
            inventory.update({name: int(count_str)})

    total_unit = 0
    for i in inventory.values():
        total_unit += i

    unique_type = len(inventory)

    print(f"Total items in inventory: {total_unit}")
    print(f"Unique item types: {unique_type}")

    print("\n=== Current Inventory ===")
    for item, count in inventory.items():
        percent = (count / total_unit) * 100
        print(f"{item}: {count} units ({percent:.1f}%)")

    most_abundant = max(inventory, key=inventory.get)
    least_abundant = min(inventory, key=inventory.get)

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant} ({inventory[most_abundant]} units)")
    print(f"Least abundant: {least_abundant} ({inventory[least_abundant]}"
          " units)")

    categories = {
        "Moderate": {},
        "Scarce": {}
    }

    for item, count in inventory.items():
        if count > 3:
            categories["Moderate"][item] = count
        else:
            categories["Scarce"][item] = count

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    restock_needed = []

    for item, count in inventory.items():
        if count < 2:
            restock_needed.append(item)

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")

    has_sword = 'sword' in inventory
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


if __name__ == "__main__":
    inventory_system()
