"""
This module simulates crisis response scenarios for accessing data archives,
including error handling for various exceptions.
"""


def ft_crisis_response(filename):
    """
    Simulates crisis response for accessing data archives with error handling.
    """
    print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, 'r') as archive:
            content = archive.read().strip()
            # content = content + 5
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, check logs")


def start_crisis_response():
    """
    Initiates crisis response scenarios for data archive access.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    test = [
        "lost_archive.txt",
        "classified_vault.txt"
    ]
    for file in test:
        ft_crisis_response(file)
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")

    try:
        with open("standard_archive.txt", 'r') as f:
            print(f"SUCCESS: Archive recovered - \"{f.read().strip()}\"")
            print("STATUS: Normal operations resumed")
    except Exception as e:
        print(f"Error: {e}")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    start_crisis_response()
