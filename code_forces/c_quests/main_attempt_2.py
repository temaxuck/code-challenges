def solution(n, k, a, b):
    a_sum, b_max, exp = 0, 0, 0

    for i in range(min(n, k)):
        a_sum += a[i]
        b_max = max(b_max, b[i])
        exp = max(exp, a_sum + b_max * (k - i - 1))

    return exp


def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        print(solution(n, k, a, b))


if __name__ == "__main__":
    main()
