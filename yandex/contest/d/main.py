from typing import Tuple

COMMANDS = "FLR"


def change_position(
    command: str,
    memo: dict,
    current_position: int = 0,
    current_direction: str = "R",
) -> Tuple[int, int]:

    if (command, current_position, current_direction) in memo:
        print("hit cache")
        return memo[(command, current_position, current_direction)]

    initial_position, initial_direction = current_position, current_direction

    if command == "F":
        if current_direction == "R":
            current_position += 1
        elif current_direction == "L":
            current_position -= 1
    else:
        current_direction = command

    memo[(command, initial_position, initial_direction)] = (
        current_position,
        current_direction,
    )

    return current_position, current_direction


def get_updated_position(
    commands: str, memo: dict, current_position: int = 0, current_direction: str = "R"
):
    for command in commands:
        current_position, current_direction = change_position(
            command, memo, current_position, current_direction
        )

    return current_position


def get_possible_positions(player_commands):
    n = len(player_commands)
    possible_positions = set()
    memo = {}

    stack = [(0, False, 0, "R")]

    while stack:
        i, changed, current_pos, current_direction = stack.pop()

        if changed:
            possible_positions.add(
                get_updated_position(
                    player_commands[i:],
                    memo,
                    current_pos,
                    current_direction,
                )
            )
            continue

        for possible_command in COMMANDS:
            if possible_command == player_commands[i] and i == n - 1:
                continue

            if possible_command == player_commands[i]:
                new_pos, new_dir = change_position(
                    possible_command, memo, current_pos, current_direction
                )
                stack.append((i + 1, False, new_pos, new_dir))
            else:
                new_pos, new_dir = change_position(
                    possible_command, memo, current_pos, current_direction
                )
                stack.append((i + 1, True, new_pos, new_dir))

    print(memo)

    return possible_positions


if __name__ == "__main__":
    from datetime import datetime

    N = int(input())
    player_commands = input()

    start = datetime.now()

    possible_positions = get_possible_positions(player_commands)
    print(len(possible_positions))

    end = datetime.now()
    print(end - start)
