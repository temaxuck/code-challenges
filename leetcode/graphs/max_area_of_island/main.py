from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        WIDTH, HEIGHT = len(grid[0]), len(grid)
        max_area = 0

        def bfs(start_x, start_y):
            dq = deque([(start_x, start_y)])
            current_area = 0

            while dq:
                x, y = dq.popleft()
                current_area += 1

                t = (x, y - 1) if 0 <= y - 1 < HEIGHT and grid[y - 1][x] else None
                b = (x, y + 1) if 0 <= y + 1 < HEIGHT and grid[y + 1][x] else None
                l = (x - 1, y) if 0 <= x - 1 < WIDTH and grid[y][x - 1] else None
                r = (x + 1, y) if 0 <= x + 1 < WIDTH and grid[y][x + 1] else None

                for point in [t, r, b, l]:
                    if point:
                        px, py = point
                        grid[py][px] = 0
                        dq.append(point)
            return current_area

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    area = bfs(x, y)
                    max_area = max(area, max_area)

        return max_area


print(
    Solution().maxAreaOfIsland(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
    )
)

# PASSED
# print(
#     Solution().maxAreaOfIsland(
#         [
#             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#         ]
#     )
# )
