"""
This module manages multiple data streams for a communication system.
"""


import sys
"""imort sys for stream management"""


def streams():
    """
    Manages multiple data streams for a communication system.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    print("\nInput Stream active. Enter archivist ID: ", end="")
    archivist_id = input()

    print("Input Stream active. Enter status report: ", end="")
    status_report = input()
    sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                     f"{status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                     " verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    streams()
