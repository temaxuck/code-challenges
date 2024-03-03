def min_cost(row, col, field, N, M, memo={}):
    if (row, col) in memo:
        return memo[(row, col)]

    if row == N - 1 and col == M - 1:
        memo[(row, col)] = field[row][col]
        return field[row][col]

    if row == N - 1:
        result = min_cost(row, col + 1, field, N, M) + field[row][col]
        memo[(row, col)] = result
        return result

    if col == M - 1:
        result = min_cost(row + 1, col, field, N, M) + field[row][col]
        memo[(row, col)] = result
        return result

    result = (
        min(
            min_cost(row + 1, col, field, N, M),
            min_cost(row, col + 1, field, N, M),
        )
        + field[row][col]
    )
    memo[(row, col)] = result
    return result


def main():
    N, M = map(int, input().split())
    field = []

    for _ in range(N):
        field_row = list(map(int, input().split()))
        field.append(field_row)

    print(min_cost(0, 0, field, N, M))


if __name__ == "__main__":
    main()
