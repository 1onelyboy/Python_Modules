import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        parts_count = 0
        coord = input("Enter new coordinates as floats in format 'x,y,z': ")
        s = coord.replace(" ", "")
        parts = s.split(",")
        for part in parts:
            parts_count += 1
        if parts_count != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError:
            for part in parts:
                try:
                    float(part)
                except ValueError as e:
                    print(f"Error on parameter '{part}': {e}")


def calculate_distance(p1: tuple[float, float, float],
                       p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x1, y1, z1 = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    center = (0.0, 0.0, 0.0)
    distance = calculate_distance(pos1, center)
    print(f"Distance to center: {round(distance, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    distance = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
