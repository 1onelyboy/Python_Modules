from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (lambda target, power: spell(target, power) if
            condition(target, power) else "Spell fizzled")


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [s(target, power) for s in spells]


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def hammer(target: str, power: int) -> str:
    return f"Hammer smashes {target} for {power} HP"


def greater_than(target: str, power: int) -> bool:
    return power >= 20


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    a, b = combined("Dragon", 50)
    print(f"Combined spell result: {a}, {b}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball("Dragon", 10)}, "
          f"Amplified: {mega_fireball("Dragon", 10)}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(greater_than, fireball)
    print(f"Case 1: {conditional("Dragon", 22)}")
    print(f"Case 2: {conditional("Dragon", 8)}")

    print("\nTesting spell sequence...")
    lst = spell_sequence([heal, fireball, hammer])
    ls = lst("Dragon", 25)
    for i in ls:
        print(i)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
