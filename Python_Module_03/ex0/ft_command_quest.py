import sys


def command_quest() -> None:
    args = sys.argv
    total_arguments = len(sys.argv)

    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if total_arguments == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_arguments - 1}")
        i = 1
        for arg in args[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {total_arguments}")


if __name__ == "__main__":
    command_quest()
