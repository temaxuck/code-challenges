def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def solution(a, b):
    if b % a == 0:
        return b // a * b

    return int((a * b) / min((b % a), gcd(a, b)))


def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(solution(a, b))


if __name__ == "__main__":
    main()
