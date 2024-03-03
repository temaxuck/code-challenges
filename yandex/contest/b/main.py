from bisect import bisect_left

if __name__ == "__main__":
    N, Q = map(int, input().split())
    dictionary = []

    for _ in range(N):
        dictionary.append(input().strip())

    for _ in range(Q):
        k, p = input().split()
        k = int(k)
        start_idx = bisect_left(dictionary, p)
        idx = start_idx + k

        if idx - 1 < N and dictionary[idx - 1].startswith(p):
            print(idx)
        else:
            print(-1)
