from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(opponents: list) -> None:
    try:
        print("*** Tournament ***")
        print(f"{len(opponents)} opponents involved")

        i = 0
        while i < len(opponents):
            factory1, strategy1 = opponents[i]

            j = i + 1
            while j < len(opponents):
                factory2, strategy2 = opponents[j]

                try:
                    c1 = factory1.create_base()
                    c2 = factory2.create_base()

                    print("\n* Battle *")
                    print(c1.describe())
                    print(" vs.")
                    print(c2.describe())
                    print(" now fight!")

                    strategy1.act(c1)
                    strategy2.act(c2)

                except Exception as e:
                    print(f"Battle error, aborting tournament: {e}")

                j += 1
            i += 1

    except Exception as e:
        print(f"Critical error, tournament stopped: {e}")


def main() -> None:
    print('Tournament 0 (basic)')
    print(' [ (Flameling+Normal), (Healing+Defensive) ]')
    battle([(FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])

    print('\nTournament 1 (error)')
    print(' [ (Flameling+Normal), (Healing+Defensive) ]')
    battle([(FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())])


if __name__ == "__main__":
    main()
