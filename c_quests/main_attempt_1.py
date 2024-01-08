def solution(n, k, a, b, memo={}, early_quit=False):
    print(n, k, a, b, memo)
    total_exp = 0

    if n == 0 or k == 0:
        return 0

    if n == 1 and k == 1:
        return a[0]

    if a == [] or b == []:
        return 0

    try:
        return memo[(n, k)]
    except KeyError:
        if k == n:
            l = solution(n - 1, k - 1, a[: n - 1], b[: n - 1], memo=memo)
            memo.update({(n - 1, k - 1): l})
            if early_quit:
                total_exp = l
            else:
                total_exp = l + a[-1]
        elif k > n:
            l, r = (
                solution(n - 1, k - 1, a[: n - 1], b[: n - 1], memo=memo),
                solution(n, k - 1, a, b, memo=memo),
            )

            memo.update({(n - 1, k - 1): l})
            memo.update({(n, k - 1): r})

            if early_quit:
                total_exp = max(l, r)
            else:
                if (result_l := l + a[-1]) > (result_r := r + max(b)):
                    total_exp = result_l
                else:
                    total_exp = result_r

    print(f"({n}, {k}): {total_exp}")

    return total_exp


def main():
    t = int(input())

    for _ in range(t):
        # n, k = map(int, input().split())
        # a = list(map(int, input().split()))
        # b = list(map(int, input().split()))

        n, k = 6, 4
        a = [1, 4, 5, 4, 5, 10]
        b = [1, 5, 1, 2, 5, 1]

        # if k <= n:
        #     a, b = a[:k], b[:k]
        #     n = k
        #     sol1, memo1 = solution(n, k, a, b, memo={})
        #     sol2, _ = solution(n - 1, k, a[: n - 1], b[: n - 1], memo=memo1)
        #     print(max(sol1, sol2), memo1)
        # else:
        if k < n:
            print(solution(k, n + 1, a[:k], b[:k], memo={}, early_quit=True))
        elif k == n:
            opt = 0
            max_i = 0
            for i in range(n):
                if (
                    result := solution(i, k + 1, a[:i], b[:i], memo={}, early_quit=True)
                ) > opt:
                    opt = result
                    max_i = i
            print(opt)
        else:
            print(solution(n, k, a, b, memo={}))


if __name__ == "__main__":
    main()
