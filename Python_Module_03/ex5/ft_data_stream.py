from typing import Generator
import random


players = ["bob", "alice", "dylan", "charlie"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(event_list: list[tuple[str, str]]) -> (
    Generator[tuple[str, str], None, None]
):
    while event_list:
        index = random.randint(0, len(event_list) - 1)
        event = event_list[index]
        event_list.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for x in range(1000):
        event = next(events)
        print(f"Event {x}: Player {event[0]} did action {event[1]}")

    event_list = []
    for i in range(10):
        event_list.append(next(events))
    print(f"\nBuilt list of 10 events: {event_list}")

    consumer = consume_event(event_list)
    for ev in consumer:
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
