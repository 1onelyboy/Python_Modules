from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    total = 0

    def plus() -> int:
        nonlocal total
        total += 1
        return total
    return plus


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def add(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return add


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item: f"{enchantment_type} {item}"


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    a = mage_counter()
    b = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}: {a()}")
    print(f"counter_b call 1: {b()}")

    print("\nTesting spell accumulator...")
    n = 100
    a1 = 20
    a2 = 30
    add = spell_accumulator(n)
    print(f"Base {n}, add {a1}: {add(a1)}")
    print(f"Base {n}, add {a2}: {add(a2)}")

    print("\nTesting enchantment factory...")
    e1 = enchantment_factory("Flaming")
    e2 = enchantment_factory("Frozen")
    print(e1("Sword"))
    print(e2("Shield"))

    print("\nTesting memory vault...")
    mv = memory_vault()
    print("Store 'secret' = 42")
    mv['store']("secret", 42)
    print(f"Recall 'secret': {mv['recall']("secret")}")
    print(f"Recall 'unknown': {mv['recall']("unknown")}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
