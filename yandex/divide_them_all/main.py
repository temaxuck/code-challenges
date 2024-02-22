"""
INPUT SAMPLES:
======================
3 rectangles:
----------------------
3
1 1 1 3 1 3 3 1 3
1 4 4 6 4 6 6 4 6
1 6 6 12 6 12 12 6 12
----------------------
"Yes"
======================
3 circles:
----------------------
3
0 1 1 1	
0 2 2 2	
0 3 3 3
----------------------
"Yes"
======================
1 rectangle, 2 circles:
----------------------
3	
1 0 0 0 1 1 1 1 0	
0 10 10 10	
0 1 2 3
----------------------
"No"
"""

if __name__ == "__main__":
    n = int(input())
    targets_centers = []

    for i in range(n):
        target_type, *taget_properties = map(int, input().split())
        if target_type == 0:
            radius, *center = taget_properties
            targets_centers.append(center)
        elif target_type == 1:
            vertices = taget_properties
            targets_centers.append(
                [
                    (vertices[0 * 2 + 0] + vertices[2 * 2 + 0]) / 2,
                    (vertices[0 * 2 + 1] + vertices[2 * 2 + 1]) / 2,
                ]
            )

    if len(targets_centers) < 3:
        print("Yes")
        exit(0)

    # y = k * x + c
    x0, y0 = targets_centers[0]
    k = abs(
        (targets_centers[0][1] - targets_centers[1][1])
        / (targets_centers[0][0] - targets_centers[1][0])
    )
    c = y0 - k * x0

    for target_center in targets_centers[2:]:
        if target_center[1] != k * target_center[0] + c:
            print("No")
            exit(0)

    print("Yes")
