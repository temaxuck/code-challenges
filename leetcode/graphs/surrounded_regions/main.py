from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        WIDTH, HEIGHT = len(board[0]), len(board)

        # find "O"s on horizontal edges
        for x in range(WIDTH):
            if board[0][x] in ["O", "O!"]:
                board[0][x] = "O!"
                y = 1
                while y < HEIGHT:
                    if board[y][x] != "O":
                        break
                    board[y][x] = "O!"
                    y += 1

            if board[HEIGHT - 1][x] in ["O", "O!"]:
                board[HEIGHT - 1][x] = "O!"
                y = HEIGHT - 2
                while y >= 0:
                    if board[y][x] != "O":
                        break
                    board[y][x] = "O!"
                    y -= 1

        # find "O"s on vertical edges
        for y in range(HEIGHT):
            if board[y][0] in ["O", "O!"]:
                board[y][0] = "O!"
                x = 1
                while x < WIDTH:
                    if board[y][x] != "O":
                        break
                    board[y][x] = "O!"
                    x += 1

            if board[y][WIDTH - 1] in ["O", "O!"]:
                board[y][WIDTH - 1] = "O!"
                x = WIDTH - 2
                while x >= 0:
                    if board[y][x] != "O":
                        break
                    board[y][x] = "O!"
                    x -= 1

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "O!":
                    board[y][x] = "O"


board = [
    ["O", "X", "X", "O", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "O", "X", "O", "X"],
    ["O", "X", "O", "O", "O"],
    ["X", "X", "O", "X", "O"],
]
Solution().solve(board)
for row in board:
    print(row)
