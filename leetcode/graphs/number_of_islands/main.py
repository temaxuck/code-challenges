from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0
        dq = deque([])

        def bfs(start_x, start_y):
            dq = deque([(start_x, start_y)])

            while dq:
                x, y = dq.popleft()
                for adj_x, adj_y in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                    if 0 <= adj_x < n and 0 <= adj_y < m and grid[adj_y][adj_x] == "1":
                        grid[adj_y][adj_x] = "0"
                        dq.append((adj_x, adj_y))

        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    grid[y][x] = "0"
                    bfs(x, y)
                    islands += 1

        return islands


# print(
#     Solution().find_adjacent_lands(
#         [
#             ["1", "1", "1", "1", "0"],
#             ["1", "1", "0", "1", "0"],
#             ["1", "1", "0", "0", "0"],
#             ["0", "0", "0", "0", "0"],
#         ],
#         (3, 0),
#     )
# )
print(
    Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
