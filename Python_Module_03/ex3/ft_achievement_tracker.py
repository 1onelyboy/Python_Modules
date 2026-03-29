import random


all_achievements_list = [
    'Crafting Genius', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer',
    'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps',
    'Sharp Mind', 'Hidden Path Finder', 'Legendary Hero'
]


def gen_player_achievements(achievements_list: list[str]) -> set[str]:
    num_achievements = random.randint(3, len(achievements_list))
    return set(random.sample(achievements_list, num_achievements))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements(all_achievements_list)
    bob = gen_player_achievements(all_achievements_list)
    charlie = gen_player_achievements(all_achievements_list)
    dylan = gen_player_achievements(all_achievements_list)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct = set.union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")

    common_achievements = set.intersection(alice, bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    full_set = set(all_achievements_list)
    print(f"\nAlice is missing: {full_set.difference(alice)}")
    print(f"Bob is missing: {full_set.difference(bob)}")
    print(f"Charlie is missing: {full_set.difference(charlie)}")
    print(f"Dylan is missing: {full_set.difference(dylan)}")


if __name__ == "__main__":
    main()
