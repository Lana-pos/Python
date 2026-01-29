"""
Exercise to demonstrate command-line argument handling in Python.
"""


import sys
"""this module handles command-line arguments"""


def command_quest():
    """
    Main function to demonstrate command-line argument handling.
    """
    print("=== Command Quest ===")
    total_len = len(sys.argv)

    if total_len == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total_len}")

    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total_len - 1}")
        for i in range(1, total_len):
            print(f"Arguments {i}: {sys.argv[i]}")

        print(f"Total arguments: {total_len}")


if __name__ == "__main__":
    command_quest()
