"""
A module that demonstrates a simple coordinate system for a game.
It includes functions to parse coordinates, calculate distances, and
showcase tuple unpacking.
"""


import math
"""
math module is used to perform mathematical calculations like square root
"""


def parse_argum(coordinate) -> tuple | None:
    """
    Parses a coordinate string in the format "x,y,z" into a tuple of integers.
    Returns None if parsing fails, with error details printed.
    """
    try:
        coord = coordinate.split(",")
        x = int(coord[0])
        y = int(coord[1])
        z = int(coord[2])

        return (x, y, z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def calc_distance(t1: tuple, t2: tuple):
    """
    Calculates the Euclidean distance between two 3D points represented
    as tuples.
    """
    x1, y1, z1 = t1
    x2, y2, z2 = t2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return (distance)


def coordinate_system():
    """
    Main function to demonstrate coordinate parsing, distance calculation,
    and tuple unpacking.
    """
    print("=== Game Coordinate System ===")
    p1 = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"\nPosition created: {p1}")
    dist1 = calc_distance(origin, p1)
    print(f"Distance between {origin} and {p1}: {dist1:.2f}")

    coord_input = "3,4,0"
    print(f"\nParsing coordinates: \"{coord_input}\"")
    p2 = parse_argum(coord_input)

    if p2:
        print(f"Parsed position: {p2}")
        dist2 = calc_distance(origin, p2)
        print(f"Distance between {origin} and {p2}: {dist2:.1f}")

        print("\nParsing invalid coordinates: \"abc,def,ghi\"")
        parse_argum("abc,def,ghi")

        print("\nUnpacking demonstration:")
        x, y, z = p2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system()
