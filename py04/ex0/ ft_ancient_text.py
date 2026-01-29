"""
This script simulates a data recovery system that retrieves and displays
information from a specified storage vault. It includes error handling for
cases where the storage vault does not exist.
"""


def recover_data():
    """
    Simulates the recovery of data from a storage vault.
    """
    filename = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {filename}")

    try:
        file = open(filename, 'r')
        print("Connection established...")
        print("\nRECOVERED DATA:")
        content = file.read()
        print(content.strip())
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_data()
