from functools import reduce

NUMERATOR = 2023


def solution(n, k, b):
    b_product = reduce(lambda a, b: a * b, b)

    if NUMERATOR % b_product != 0:
        return None

    if NUMERATOR == b_product:
        return [1] * k
    else:
        return [NUMERATOR // b_product] + [1] * max(k - 1, 0)


def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        b = list(map(int, input().split()))

        if not (result := solution(n, k, b)):
            print("NO")
        else:
            print("YES")
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
