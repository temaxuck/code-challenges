def max_cost_path(row, col, field, N, M, memo={}):
    if (row, col) in memo:
        return memo[(row, col)]

    if row == N - 1 and col == M - 1:
        memo[(row, col)] = field[row][col], []
        return field[row][col], []

    if row == N - 1:
        score, path = max_cost_path(row, col + 1, field, N, M, memo)
        result = score + field[row][col], [*["R"], *path]
        memo[(row, col)] = result
        return result

    if col == M - 1:
        score, path = max_cost_path(row + 1, col, field, N, M, memo)
        result = score + field[row][col], [*["D"], *path]
        memo[(row, col)] = result
        return result

    score1, path1 = max_cost_path(row + 1, col, field, N, M, memo)
    score2, path2 = max_cost_path(row, col + 1, field, N, M, memo)

    if score1 > score2:
        result = score1 + field[row][col], [*["D"], *path1]
    else:
        result = score2 + field[row][col], [*["R"], *path2]

    memo[(row, col)] = result
    return result


def main():
    N, M = map(int, input().split())
    field = []

    for _ in range(N):
        field_row = list(map(int, input().split()))
        field.append(field_row)

    score, path = max_cost_path(0, 0, field, N, M)
    print(score, " ".join(path), sep="\n")


if __name__ == "__main__":
    main()
