def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])
    min_power = min(mages, key=lambda x: x['power'])
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': avg_power
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'magic'},
        {'name': 'Fire Staff',   'power': 92, 'type': 'fire'}
    ]

    mages = [
        {'name': 'Gandalf', 'power': 95, 'element': 'fire'},
        {'name': 'Merlin', 'power': 88, 'element': 'arcane'},
        {'name': 'Morgana', 'power': 72, 'element': 'dark'},
        {'name': 'Radagast', 'power': 65, 'element': 'nature'},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) comes before "
          f"{sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = (" ").join(spell_transformer(spells))
    print(transformed)

    print("\nTesting power filter...")
    filtered_mages = power_filter(mages, 75)
    print("Mages with power >= 75:")
    for mage in filtered_mages:
        print(f"{mage['name']} has {mage['power']} power")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
