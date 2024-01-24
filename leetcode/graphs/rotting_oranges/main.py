from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        WIDTH, HEIGHT = len(grid[0]), len(grid)
        to_check = set()
        rotten_oranges = set()
        time = 0

        for row in range(HEIGHT):
            for col in range(WIDTH):
                if grid[row][col] == 1:
                    to_check.add((row, col))
                if grid[row][col] == 2:
                    rotten_oranges.add((row, col, 0))

        def bfs():
            time = 0
            dq = deque(rotten_oranges)

            while dq:
                next_dq = deque([])
                while dq:
                    r, c, cur_time = dq.popleft()
                    time = max(cur_time, time)

                    top = (r - 1, c) if 0 <= r - 1 < HEIGHT else None
                    left = (r, c - 1) if 0 <= c - 1 < WIDTH else None
                    right = (r, c + 1) if 0 <= c + 1 < WIDTH else None
                    bottom = (r + 1, c) if 0 <= r + 1 < HEIGHT else None

                    for p in (top, left, right, bottom):
                        if p:
                            p_row, p_col = p
                            if grid[p_row][p_col] == 1:
                                next_dq.append((p_row, p_col, cur_time + 1))
                                grid[p_row][p_col] = 3
                                if (p_row, p_col) in to_check:
                                    to_check.remove((p_row, p_col))
                            elif grid[p_row][p_col] == 2:
                                next_dq.append((p_row, p_col, cur_time))
                                grid[p_row][p_col] = 3
                # yield next_dq
                dq = next_dq

            return time

        # print(next(bfs()))
        time = bfs()

        if to_check:
            return -1

        return time


# grid = [
#     [0, 2, 2],
# ]

# Passed:
# grid = [
#     [2, 1, 1],
#     [1, 1, 1],
#     [0, 1, 2],
# ]

# grid = [
#     [0, 1, 2],
#     [1, 0, 1],
#     [0, 1, 1],
# ]

# grid = [
#     [2, 1, 1],
#     [0, 1, 1],
#     [1, 0, 1],
# ]

# Passed
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]

print(Solution().orangesRotting(grid))
