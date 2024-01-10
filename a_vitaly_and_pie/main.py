def solution(n, s):
    keys = [0] * 26
    keys_to_buy = 0

    for i in range(0, len(s), 2):
        key = s[i]
        door = s[i + 1]
        keys[ord(key) - 97] += 1

        if keys[(index := (ord(door.lower()) - 97))] == 0:
            keys_to_buy += 1
        else:
            keys[index] -= 1

    return keys_to_buy


def main():
    n = int(input())
    s = input()

    print(solution(n, s))


if __name__ == "__main__":
    main()
