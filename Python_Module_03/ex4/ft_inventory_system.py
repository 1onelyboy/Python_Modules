import sys


def parse_input(args: list[str]) -> dict[str, int] | None:
    dictionary = {}
    for arg in args[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = parts[0], parts[1]
        if key in dictionary:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            dictionary[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return dictionary if dictionary else None


def inventory_statistics(dictionary: dict[str, int]) -> None:
    max_key = None
    max_value = None
    min_key = None
    min_value = None
    for key in dictionary:
        value = dictionary[key]
        if max_value is None or max_value < value:
            max_value = value
            max_key = key
        if min_value is None or min_value > value:
            min_value = value
            min_key = key
    print(f"Item most abundant: {max_key} with quantity {max_value}")
    print(f"Item least abundant: {min_key} with quantity {min_value}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_input(sys.argv)
    if not inventory:
        print("No valid inventory data provided")
        return
    else:
        print(f"Got inventory: {inventory}")

    items_list = list(inventory.keys())
    quantity_total = sum(inventory.values())
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(inventory)} items: {quantity_total}")

    for key in inventory:
        value = inventory[key]
        percentage = (value / quantity_total) * 100
        print(f"Item {key} represents {round(percentage, 1)}%")

    inventory_statistics(inventory)

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
