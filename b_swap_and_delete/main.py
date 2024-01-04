def solution(s):
    if len(s) < 2:
        return len(s)

    char_count = {"0": 0, "1": 0}

    for character in s:
        char_count[character] += 1

    if char_count["0"] == char_count["1"]:
        return 0

    t_length = 0
    most_entries = 0
    least_char, most_char = (
        min(char_count.items(), key=lambda x: x[1]),
        max(char_count.items(), key=lambda x: x[1]),
    )

    for i in range(len(s)):
        if s[i] == most_char[0]:
            most_entries += 1
            if most_entries > char_count[least_char[0]]:
                break
        t_length += 1

    return len(s) - t_length


def main():
    t = int(input())

    for _ in range(t):
        s = input()
        print(solution(s))


if __name__ == "__main__":
    main()
