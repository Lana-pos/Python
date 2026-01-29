"""
This module demonstrates handling various built-in exceptions in Python
related to garden operations, such as invalid input, division by zero,
file not found, and key errors in dictionaries.
"""


def garden_operations() -> None:
    """
    Perform various garden operations that may raise different exceptions.
    """
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        dictEr = {"lemon": "yellow"}
        print(dictEr["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        15 / 0
    except (ValueError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types():
    """
    Test various built-in error types in garden operations.
    """
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
