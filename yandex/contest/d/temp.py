COMMANDS = "FLR"


def calculate_position(
    player_commands: str,
    memo: dict,
    current_direction: str = "R",
    current_position: int = 0,
) -> int:
    if player_commands in memo:
        return memo[player_commands]

    for command in player_commands:
        if command == "F":
            if current_direction == "R":
                current_position += 1
            elif current_direction == "L":
                current_position -= 1
        else:
            current_direction = command

    memo[player_commands] = current_position
    return current_position


def get_possible_positions(player_commands):
    n = len(player_commands)
    possible_positions = set()
    memo = {}

    stack = [(0, None, False)]

    while stack:
        i, new_command, changed = stack.pop()

        if changed:
            possible_positions.add(
                calculate_position(
                    player_commands[: i - 1] + new_command + player_commands[i:], memo
                )
            )
            continue

        for possible_command in COMMANDS:
            if possible_command == player_commands[i] and i == n - 1:
                continue

            if possible_command == player_commands[i] and i < n - 1:
                stack.append((i + 1, possible_command, False))
            else:
                stack.append((i + 1, possible_command, True))

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
