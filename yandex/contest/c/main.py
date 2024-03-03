def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


if __name__ == "__main__":
    N = int(input())
    coordinates = []
    non_overlapping_count = 0

    for _ in range(N):
        a, b = map(int, input().split())
        coordinates.append((a, b))

    # sort coordinates by endpoint b
    coordinates.sort(key=lambda x: x[1])

    print(coordinates)

    last_end = coordinates[0][1]

    for a, b in coordinates[1:]:
        if a > last_end:
            last_end = b
            non_overlapping_count += 1
        # if a <= last_end:
        #     non_overlapping_count = max(0, non_overlapping_count - 1)

    print(non_overlapping_count)
