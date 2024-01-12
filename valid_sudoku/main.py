from typing import List


class Solution:
    BOARD_DIMENSION = 9
    SUB_BOXES_DIMENSION = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(self.BOARD_DIMENSION):
            s = set()
            for c in range(self.BOARD_DIMENSION):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in s:
                    return False
                s.add(cell)

        for c in range(self.BOARD_DIMENSION):
            s = set()
            for r in range(self.BOARD_DIMENSION):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in s:
                    return False
                s.add(cell)

        for x in range(0, self.BOARD_DIMENSION, self.SUB_BOXES_DIMENSION):
            for y in range(0, self.BOARD_DIMENSION, self.SUB_BOXES_DIMENSION):
                s = set()
                for i in range(0, self.SUB_BOXES_DIMENSION):
                    for j in range(0, self.SUB_BOXES_DIMENSION):
                        cell = board[x + i][y + j]
                        if cell == ".":
                            continue
                        if cell in s:
                            return False
                        s.add(cell)
        return True


print(
    Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
