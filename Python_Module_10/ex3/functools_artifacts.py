from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    elif operation == "add":
        return reduce(operator.add, spells)
    elif operation == "mul":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        raise Exception("Invalid operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "snow": partial(base_enchantment, 50, "Snow"),
        "water": partial(base_enchantment, 50, "Water"),
        "ice": partial(base_enchantment, 50, "Ice")
    }


def enchants(power: int, element: str, target: str) -> str:
    return f"{element} enchantement hits {target} for {power} HP"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 1:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def spell(par: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def i(par: int) -> str:
        return f"Damage spell: {par} damage"

    @spell.register(str)
    def s(par: str) -> str:
        return f"Enchantment: {par}"

    @spell.register(list)
    def ls(par: list) -> str:
        return f"Multi-cast {len(par)} spells"

    return spell


def main() -> None:
    print("\nTesting spell reducer...")
    try:
        lst = [10, 20, 30, 40]
        print(f"Sum: {spell_reducer(lst, "add")}")
        print(f"Product: {spell_reducer(lst, "mul")}")
        print(f"Max: {spell_reducer(lst, "max")}")
        print(f"Min: {spell_reducer(lst, "min")}")
    except Exception as e:
        print(e)

    print("\nTesting partial enchanter...")
    enchts = partial_enchanter(enchants)
    print(enchts["snow"]("Dragon"))
    print(enchts["water"]("Monster"))
    print(enchts["ice"]("Zombie"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    s = spell_dispatcher()
    print(s(42))
    print(s("fireball"))
    print(s(["a", "b", "c"]))
    print(s(None))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
