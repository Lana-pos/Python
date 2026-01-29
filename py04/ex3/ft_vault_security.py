"""
This module simulates secure access to a vault containing classified data.
"""


def ft_vault_security():
    """
    This function uses context managers to securely read from and write to a
    classified data vault.
    It ensures that the vault is properly sealed after operations.
    """
    filename = "classified_data.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print("\nSECURE EXTRACTION:")

    with open(filename, 'r') as vault:
        content = vault.read()
        print(content.strip())
    print("\nSECURE PRESERVATION:")
    with open(filename, 'a') as vault:
        new_data = "[CLASSIFIED] New security protocols archived"
        vault.write("\n" + new_data)
        print(new_data)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
